import bmesh
import bpy
import rna_keymap_ui
from mathutils import Vector

from . import translation

VERT_MATCH_EPSILON = 0.0001
COORD_KEY_DIGITS = 6
ADDON_MODULE = __package__ or __name__


def _safe_normalized(vector):
    if vector.length < VERT_MATCH_EPSILON:
        return Vector()
    return vector.normalized()


def _coord_key(co):
    return (
        round(co.x, COORD_KEY_DIGITS),
        round(co.y, COORD_KEY_DIGITS),
        round(co.z, COORD_KEY_DIGITS),
    )


def _build_old_vert_lookup(verts):
    lookup = {}
    for vert in verts:
        lookup.setdefault(_coord_key(vert.co), []).append(vert)
    return lookup


def _take_matching_old_vert(new_vert, old_vert_lookup):
    key = _coord_key(new_vert.co)
    candidates = old_vert_lookup.get(key, [])

    if candidates:
        if len(candidates) == 1:
            return candidates.pop()

        best_index = None
        best_distance = float("inf")
        for index, old_vert in enumerate(candidates):
            distance = (old_vert.co - new_vert.co).length
            if distance < best_distance:
                best_distance = distance
                best_index = index

        if best_index is not None and best_distance <= VERT_MATCH_EPSILON:
            return candidates.pop(best_index)

    # Fallback for precision mismatch between copied vertices.
    best_key = None
    best_index = None
    best_distance = float("inf")
    for lookup_key, lookup_candidates in old_vert_lookup.items():
        for index, old_vert in enumerate(lookup_candidates):
            distance = (old_vert.co - new_vert.co).length
            if distance < best_distance:
                best_distance = distance
                best_key = lookup_key
                best_index = index

    if best_key is not None and best_distance <= VERT_MATCH_EPSILON:
        return old_vert_lookup[best_key].pop(best_index)

    return None


def _update_edit_mesh(mesh, topology_changed):
    bmesh.update_edit_mesh(
        mesh,
        loop_triangles=topology_changed,
        destructive=topology_changed,
    )


def _update_edit_mesh_fast(mesh):
    bmesh.update_edit_mesh(mesh, loop_triangles=False, destructive=False)


def _restore_bmesh_from_backup(bm, backup_bm, mesh):
    if backup_bm is None:
        return

    bm.clear()
    temp_mesh = bpy.data.meshes.new("__omnioutset_restore")
    try:
        backup_bm.to_mesh(temp_mesh)
        bm.from_mesh(temp_mesh)
    finally:
        bpy.data.meshes.remove(temp_mesh)

    _update_edit_mesh(mesh, topology_changed=True)


def _free_backup(operator):
    backup = getattr(operator, "_bm_backup", None)
    if backup is not None:
        backup.free()
        operator._bm_backup = None


def _compute_face_extrude_data(sel_faces):
    sel_face_set = set(sel_faces)

    has_unselected_neighbor = any(
        (not link_face.select)
        for face in sel_faces
        for edge in face.edges
        for link_face in edge.link_faces
    )

    top_verts = list({vert for face in sel_faces for vert in face.verts})

    vert_normals = {}
    for vert in top_verts:
        normal_sum = Vector()
        for link_face in vert.link_faces:
            if link_face in sel_face_set:
                normal_sum += link_face.normal
        vert_normals[vert] = _safe_normalized(normal_sum)

    selected_edges = {edge for face in sel_faces for edge in face.edges}
    boundary_edges = [
        edge
        for edge in selected_edges
        if sum(1 for face in edge.link_faces if face in sel_face_set) == 1
    ]
    boundary_edge_set = set(boundary_edges)

    boundary_verts = list({vert for edge in boundary_edges for vert in edge.verts})

    vert_outward_vectors = {}
    for vert in boundary_verts:
        connected_boundary_edges = [
            edge for edge in vert.link_edges if edge in boundary_edge_set
        ]

        outward_normals = []
        for edge in connected_boundary_edges:
            face = next((f for f in edge.link_faces if f in sel_face_set), None)
            if face is None:
                continue

            for loop in face.loops:
                if loop.edge == edge:
                    edge_vector = loop.link_loop_next.vert.co - loop.vert.co
                    if edge_vector.length >= VERT_MATCH_EPSILON:
                        tangent = edge_vector.normalized()
                        outward = tangent.cross(face.normal)
                        if outward.length >= VERT_MATCH_EPSILON:
                            outward_normals.append(outward.normalized())
                    break

        if len(outward_normals) >= 2:
            normal_1, normal_2 = outward_normals[:2]
            bisector = normal_1 + normal_2
            if bisector.length < VERT_MATCH_EPSILON:
                vert_outward_vectors[vert] = normal_1
            else:
                bisector.normalize()
                cos_theta = max(0.01, normal_1.dot(bisector))
                factor = min(3.0, 1.0 / cos_theta)
                vert_outward_vectors[vert] = bisector * factor
        elif len(outward_normals) == 1:
            vert_outward_vectors[vert] = outward_normals[0]

    return has_unselected_neighbor, top_verts, vert_normals, vert_outward_vectors


def _compute_edge_extrude_data(sel_edges):
    sel_edge_set = set(sel_edges)
    sel_verts = list({vert for edge in sel_edges for vert in edge.verts})

    vert_outward_vectors = {}
    vert_z_vectors = {}

    for vert in sel_verts:
        connected_sel_edges = [edge for edge in vert.link_edges if edge in sel_edge_set]
        outward_normals = []
        z_normals = []

        for edge in connected_sel_edges:
            if not edge.link_faces:
                continue

            face = edge.link_faces[0]
            z_normals.append(face.normal)

            for loop in face.loops:
                if loop.edge == edge:
                    edge_vector = loop.link_loop_next.vert.co - loop.vert.co
                    if edge_vector.length >= VERT_MATCH_EPSILON:
                        tangent = edge_vector.normalized()
                        outward = tangent.cross(face.normal)
                        if outward.length >= VERT_MATCH_EPSILON:
                            outward_normals.append(outward.normalized())
                    break

        if len(outward_normals) >= 2:
            normal_1, normal_2 = outward_normals[:2]
            bisector = normal_1 + normal_2
            if bisector.length > VERT_MATCH_EPSILON:
                bisector.normalize()
                factor = 1.0 / max(0.01, normal_1.dot(bisector))
                vert_outward_vectors[vert] = bisector * factor
            else:
                vert_outward_vectors[vert] = normal_1
        elif outward_normals:
            vert_outward_vectors[vert] = outward_normals[0]

        if z_normals:
            z_sum = sum(z_normals, Vector())
            vert_z_vectors[vert] = _safe_normalized(z_sum)
        else:
            vert_z_vectors[vert] = Vector((0.0, 0.0, 1.0))

    return vert_outward_vectors, vert_z_vectors


# -------------------------------------------------------------------
# CORE OPERATOR: FACE EXTRUDE
# -------------------------------------------------------------------
class MESH_OT_omnioutset_face(bpy.types.Operator):
    """Interactive extrusion along face normal with equidistant edge outset"""

    bl_idname = "mesh.omnioutset_smart_face"
    bl_label = "Smart Face Extrude"
    bl_options = {"REGISTER", "UNDO", "GRAB_CURSOR", "BLOCKING"}

    extrude_dist: bpy.props.FloatProperty(name="Extrude Distance", default=0.0, step=0.01)
    outward_offset: bpy.props.FloatProperty(name="Outward Offset", default=0.0, step=0.01)

    @classmethod
    def poll(cls, context):
        return (
            context.edit_object is not None
            and context.mode == "EDIT_MESH"
            and context.tool_settings.mesh_select_mode[2]
        )

    def execute(self, context):
        obj = context.edit_object
        bm = bmesh.from_edit_mesh(obj.data)

        sel_faces = [face for face in bm.faces if face.select]
        if not sel_faces:
            self.report({"WARNING"}, "At least one face must be selected!")
            return {"CANCELLED"}

        (
            has_unselected_neighbor,
            top_verts,
            vert_normals,
            vert_outward_vectors,
        ) = _compute_face_extrude_data(sel_faces)

        ret = bmesh.ops.extrude_face_region(bm, geom=sel_faces)
        new_top_verts = [vert for vert in ret["geom"] if isinstance(vert, bmesh.types.BMVert)]

        old_vert_lookup = _build_old_vert_lookup(top_verts)
        for new_vert in new_top_verts:
            old_vert = _take_matching_old_vert(new_vert, old_vert_lookup)
            if old_vert is None:
                continue

            new_vert.co += vert_normals.get(old_vert, Vector()) * self.extrude_dist
            new_vert.co += vert_outward_vectors.get(old_vert, Vector()) * self.outward_offset

        if has_unselected_neighbor:
            bmesh.ops.delete(bm, geom=sel_faces, context="FACES")
        else:
            bmesh.ops.reverse_faces(bm, faces=sel_faces)

        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.normal_update()
        _update_edit_mesh(obj.data, topology_changed=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        self.prev_mouse_x = event.mouse_x
        self.prev_mouse_y = event.mouse_y
        self.extrude_dist = 0.0
        self.outward_offset = 0.0

        self.obj = context.edit_object
        self.bm = bmesh.from_edit_mesh(self.obj.data)
        self._bm_backup = self.bm.copy()

        sel_faces = [face for face in self.bm.faces if face.select]
        if not sel_faces:
            self.report({"WARNING"}, "At least one face must be selected!")
            _free_backup(self)
            return {"CANCELLED"}

        (
            has_unselected_neighbor,
            top_verts,
            vert_normals,
            vert_outward_vectors,
        ) = _compute_face_extrude_data(sel_faces)

        ret = bmesh.ops.extrude_face_region(self.bm, geom=sel_faces)
        new_top_verts = [vert for vert in ret["geom"] if isinstance(vert, bmesh.types.BMVert)]

        old_vert_lookup = _build_old_vert_lookup(top_verts)
        self.vert_cache = []
        for new_vert in new_top_verts:
            old_vert = _take_matching_old_vert(new_vert, old_vert_lookup)
            if old_vert is None:
                continue

            self.vert_cache.append(
                {
                    "vert": new_vert,
                    "base_co": old_vert.co.copy(),
                    "normal": vert_normals.get(old_vert, Vector()),
                    "outward": vert_outward_vectors.get(old_vert, Vector()),
                }
            )

        if has_unselected_neighbor:
            bmesh.ops.delete(self.bm, geom=sel_faces, context="FACES")
        else:
            bmesh.ops.reverse_faces(self.bm, faces=sel_faces)

        _update_edit_mesh(self.obj.data, topology_changed=True)
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type in {"RIGHTMOUSE", "ESC"}:
            _restore_bmesh_from_backup(self.bm, self._bm_backup, self.obj.data)
            _free_backup(self)
            context.workspace.status_text_set(None)
            return {"CANCELLED"}

        if event.type in {"LEFTMOUSE", "RET", "NUMPAD_ENTER"} and event.value == "PRESS":
            bmesh.ops.recalc_face_normals(self.bm, faces=self.bm.faces)
            self.bm.normal_update()
            _update_edit_mesh(self.obj.data, topology_changed=False)
            _free_backup(self)
            context.workspace.status_text_set(None)
            return {"FINISHED"}

        if event.type == "MOUSEMOVE":
            dx = event.mouse_x - self.prev_mouse_x
            dy = event.mouse_y - self.prev_mouse_y
            sensitivity = 0.001 if event.shift else 0.005

            if event.ctrl:
                self.outward_offset += dx * sensitivity
            else:
                self.extrude_dist += dy * sensitivity

            self.prev_mouse_x = event.mouse_x
            self.prev_mouse_y = event.mouse_y

            for vert_data in self.vert_cache:
                vert = vert_data["vert"]
                vert.co = (
                    vert_data["base_co"]
                    + (vert_data["normal"] * self.extrude_dist)
                    + (vert_data["outward"] * self.outward_offset)
                )

            self.bm.normal_update()
            _update_edit_mesh_fast(self.obj.data)

            translate = bpy.app.translations.pgettext_iface
            status_msg = translate(
                "OmniOutset Face | Extrude: {0:.3f} (Up/Down) | Outset: {1:.3f} (Ctrl+L/R) | [Shift] Precision | [LMB] Confirm"
            )
            context.workspace.status_text_set(
                status_msg.format(self.extrude_dist, self.outward_offset)
            )

        return {"RUNNING_MODAL"}


# -------------------------------------------------------------------
# CORE OPERATOR: EDGE EXTRUDE
# -------------------------------------------------------------------
class MESH_OT_omnioutset_edge(bpy.types.Operator):
    """Interactive equidistant outward extrusion for selected edges"""

    bl_idname = "mesh.omnioutset_edge"
    bl_label = "Equidistant Edge Extrude"
    bl_options = {"REGISTER", "UNDO", "GRAB_CURSOR", "BLOCKING"}

    outward_offset: bpy.props.FloatProperty(name="Outward Offset", default=0.0, step=0.01)
    local_z_offset: bpy.props.FloatProperty(name="Z Axis Offset", default=0.0, step=0.01)

    @classmethod
    def poll(cls, context):
        return (
            context.edit_object is not None
            and context.mode == "EDIT_MESH"
            and context.tool_settings.mesh_select_mode[1]
        )

    def execute(self, context):
        obj = context.edit_object
        bm = bmesh.from_edit_mesh(obj.data)

        sel_edges = [edge for edge in bm.edges if edge.select]
        if not sel_edges:
            self.report({"WARNING"}, "Please select boundary edges first!")
            return {"CANCELLED"}

        vert_outward_vectors, vert_z_vectors = _compute_edge_extrude_data(sel_edges)

        ret = bmesh.ops.extrude_edge_only(bm, edges=sel_edges)
        new_verts = [vert for vert in ret["geom"] if isinstance(vert, bmesh.types.BMVert)]

        for new_vert in new_verts:
            for edge in new_vert.link_edges:
                old_vert = edge.other_vert(new_vert)
                if old_vert in vert_outward_vectors:
                    new_vert.co += vert_outward_vectors[old_vert] * self.outward_offset
                    new_vert.co += vert_z_vectors[old_vert] * self.local_z_offset
                    break

        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.normal_update()
        _update_edit_mesh(obj.data, topology_changed=True)
        return {"FINISHED"}

    def invoke(self, context, event):
        self.prev_mouse_x = event.mouse_x
        self.prev_mouse_y = event.mouse_y
        self.outward_offset = 0.0
        self.local_z_offset = 0.0

        self.obj = context.edit_object
        self.bm = bmesh.from_edit_mesh(self.obj.data)
        self._bm_backup = self.bm.copy()

        sel_edges = [edge for edge in self.bm.edges if edge.select]
        if not sel_edges:
            self.report({"WARNING"}, "Please select boundary edges first!")
            _free_backup(self)
            return {"CANCELLED"}

        vert_outward_vectors, vert_z_vectors = _compute_edge_extrude_data(sel_edges)

        ret = bmesh.ops.extrude_edge_only(self.bm, edges=sel_edges)
        new_verts = [vert for vert in ret["geom"] if isinstance(vert, bmesh.types.BMVert)]

        self.vert_cache = []
        for new_vert in new_verts:
            for edge in new_vert.link_edges:
                old_vert = edge.other_vert(new_vert)
                if old_vert in vert_outward_vectors:
                    self.vert_cache.append(
                        {
                            "vert": new_vert,
                            "base_co": old_vert.co.copy(),
                            "outward": vert_outward_vectors[old_vert],
                            "z_dir": vert_z_vectors[old_vert],
                        }
                    )
                    break

        _update_edit_mesh(self.obj.data, topology_changed=True)
        context.window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type in {"RIGHTMOUSE", "ESC"}:
            _restore_bmesh_from_backup(self.bm, self._bm_backup, self.obj.data)
            _free_backup(self)
            context.workspace.status_text_set(None)
            return {"CANCELLED"}

        if event.type in {"LEFTMOUSE", "RET", "NUMPAD_ENTER"} and event.value == "PRESS":
            bmesh.ops.recalc_face_normals(self.bm, faces=self.bm.faces)
            self.bm.normal_update()
            _update_edit_mesh(self.obj.data, topology_changed=False)
            _free_backup(self)
            context.workspace.status_text_set(None)
            return {"FINISHED"}

        if event.type == "MOUSEMOVE":
            dx = event.mouse_x - self.prev_mouse_x
            dy = event.mouse_y - self.prev_mouse_y
            sensitivity = 0.001 if event.shift else 0.005

            if event.ctrl:
                self.local_z_offset += dy * sensitivity
            else:
                self.outward_offset += dx * sensitivity

            self.prev_mouse_x = event.mouse_x
            self.prev_mouse_y = event.mouse_y

            for vert_data in self.vert_cache:
                vert = vert_data["vert"]
                vert.co = (
                    vert_data["base_co"]
                    + (vert_data["outward"] * self.outward_offset)
                    + (vert_data["z_dir"] * self.local_z_offset)
                )

            self.bm.normal_update()
            _update_edit_mesh_fast(self.obj.data)

            translate = bpy.app.translations.pgettext_iface
            status_msg = translate(
                "OmniOutset Edge | Outset: {0:.3f} (L/R) | Z-Offset: {1:.3f} (Ctrl+Up/Down) | [Shift] Precision | [LMB] Confirm"
            )
            context.workspace.status_text_set(
                status_msg.format(self.outward_offset, self.local_z_offset)
            )

        return {"RUNNING_MODAL"}


# -------------------------------------------------------------------
# SMART ROUTER: UNIFIED HOTKEY CALL
# -------------------------------------------------------------------
class MESH_OT_omnioutset_smart_call(bpy.types.Operator):
    """Automatically call Face or Edge Outset based on selection mode"""

    bl_idname = "mesh.omnioutset_smart_call"
    bl_label = "Smart OmniOutset Call"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return (
            context.edit_object is not None
            and context.mode == "EDIT_MESH"
            and (
                context.tool_settings.mesh_select_mode[1]
                or context.tool_settings.mesh_select_mode[2]
            )
        )

    def invoke(self, context, event):
        del event
        select_mode = context.tool_settings.mesh_select_mode

        if select_mode[2]:
            return bpy.ops.mesh.omnioutset_smart_face("INVOKE_DEFAULT")
        if select_mode[1]:
            return bpy.ops.mesh.omnioutset_edge("INVOKE_DEFAULT")

        return {"CANCELLED"}


# -------------------------------------------------------------------
# ADDON PREFERENCES: CUSTOM HOTKEY CONFIGURATION
# -------------------------------------------------------------------
class OmniOutsetPreferences(bpy.types.AddonPreferences):
    bl_idname = ADDON_MODULE

    def draw(self, context):
        layout = self.layout
        translate = bpy.app.translations.pgettext_iface

        box = layout.box()
        box.label(text=translate("OmniOutset Shortcut Configuration"), icon="KEYINGSET")
        box.label(
            text=translate("Customize the universal hotkey for Face & Edge Extrude below:"),
            icon="INFO",
        )
        box.separator()

        wm = context.window_manager
        kc = wm.keyconfigs.user if wm else None
        if kc is None:
            box.label(text=translate("No user keyconfig found."), icon="ERROR")
            return

        km = kc.keymaps.get("Mesh")
        if km is None:
            box.label(text=translate("Mesh keymap not found."), icon="ERROR")
            return

        kmi = next(
            (
                item
                for item in km.keymap_items
                if item.idname == MESH_OT_omnioutset_smart_call.bl_idname
            ),
            None,
        )

        if kmi:
            box.context_pointer_set("keymap", km)
            rna_keymap_ui.draw_kmi([], kc, km, kmi, box, 0)
        else:
            box.label(
                text=translate("Shortcut not found. Please try restarting Blender."),
                icon="ERROR",
            )


# -------------------------------------------------------------------
# UI AND REGISTRATION
# -------------------------------------------------------------------
def menu_func(self, context):
    select_mode = context.tool_settings.mesh_select_mode

    if select_mode[1] or select_mode[2]:
        layout = self.layout
        layout.separator()

        translate = bpy.app.translations.pgettext_iface
        layout.label(text=translate("OmniOutset Tools"), icon="SHAPEKEY_DATA")

        layout.operator_context = "INVOKE_DEFAULT"
        if select_mode[2]:
            layout.operator(
                MESH_OT_omnioutset_face.bl_idname,
                text=translate("Smart Face Extrude"),
            )
        if select_mode[1]:
            layout.operator(
                MESH_OT_omnioutset_edge.bl_idname,
                text=translate("Equidistant Edge Extrude"),
            )


classes = (
    MESH_OT_omnioutset_face,
    MESH_OT_omnioutset_edge,
    MESH_OT_omnioutset_smart_call,
    OmniOutsetPreferences,
)

addon_keymaps = []


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)

    bpy.app.translations.register(ADDON_MODULE, translation.translations_dict)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon if wm else None
    if kc:
        km = kc.keymaps.new(name="Mesh", space_type="EMPTY")
        kmi = km.keymap_items.new(
            MESH_OT_omnioutset_smart_call.bl_idname,
            "E",
            "PRESS",
            shift=True,
            alt=True,
        )
        addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        try:
            km.keymap_items.remove(kmi)
        except Exception:
            pass
    addon_keymaps.clear()

    try:
        bpy.app.translations.unregister(ADDON_MODULE)
    except Exception:
        pass

    try:
        bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)
    except Exception:
        pass

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
