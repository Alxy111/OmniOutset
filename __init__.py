import bpy
import bmesh
from mathutils import Vector

from . import translation

class MESH_OT_omnioutset_face(bpy.types.Operator):
    """Extrude along face normal with equidistant edge outset"""
    bl_idname = "mesh.omnioutset_smart_face"
    bl_label = "Smart Face Extrude & Outset"
    bl_options = {'REGISTER', 'UNDO'}

    extrude_dist: bpy.props.FloatProperty(
        name="Extrude Distance",
        default=0.1,
        step=0.01,
    )
    outward_offset: bpy.props.FloatProperty(
        name="Outward Offset",
        default=0.0,
        step=0.01,
    )

    @classmethod
    def poll(cls, context):
        return (context.edit_object is not None and 
                context.mode == 'EDIT_MESH' and 
                context.tool_settings.mesh_select_mode[2])

    def execute(self, context):
        obj = context.edit_object
        bm = bmesh.from_edit_mesh(obj.data)

        sel_faces = [f for f in bm.faces if f.select]
        if not sel_faces:
            self.report({'WARNING'}, "At least one face must be selected!")
            return {'CANCELLED'}

        island_faces = set(sel_faces)
        faces_to_check = list(sel_faces)
        is_open_sheet = False

        while faces_to_check:
            f = faces_to_check.pop()
            for e in f.edges:
                if len(e.link_faces) == 1:
                    is_open_sheet = True
                    break
                for lf in e.link_faces:
                    if lf not in island_faces:
                        island_faces.add(lf)
                        faces_to_check.append(lf)
            if is_open_sheet:
                break

        top_verts = list(set(v for f in sel_faces for v in f.verts))
        v_normals = {v: sum([f.normal for f in v.link_faces if f in sel_faces], Vector()).normalized() for v in top_verts}

        boundary_edges = [e for e in set(e for f in sel_faces for e in f.edges) if sum(1 for f in e.link_faces if f in sel_faces) == 1]
        boundary_verts = list(set(v for e in boundary_edges for v in e.verts))

        has_boundaries = len(boundary_edges) > 0
        is_entire_island_selected = all(len(e.link_faces) == 1 for e in boundary_edges) if has_boundaries else True

        vert_outward_vectors = {}
        for v in boundary_verts:
            connected_bound_edges = [e for e in v.link_edges if e in boundary_edges]
            outward_normals = []
            for e in connected_bound_edges:
                face = [f for f in e.link_faces if f in sel_faces][0]
                for loop in face.loops:
                    if loop.edge == e:
                        vec = (loop.link_loop_next.vert.co - loop.vert.co).normalized()
                        outward_normals.append(vec.cross(face.normal).normalized())
                        break

            if len(outward_normals) >= 2:
                n1, n2 = outward_normals[:2]
                bisector = (n1 + n2)
                if bisector.length < 0.0001:
                    vert_outward_vectors[v] = n1
                else:
                    bisector.normalize()
                    cos_theta = max(0.01, n1.dot(bisector))
                    vert_outward_vectors[v] = bisector / cos_theta
            elif len(outward_normals) == 1:
                vert_outward_vectors[v] = outward_normals[0]

        ret = bmesh.ops.extrude_face_region(bm, geom=sel_faces)
        new_top_verts = [v for v in ret['geom'] if isinstance(v, bmesh.types.BMVert)]

        for v_new in new_top_verts:
            match_v_old = next((v for v in top_verts if (v.co - v_new.co).length < 0.0001), None)
            if match_v_old:
                v_new.co += v_normals[match_v_old] * self.extrude_dist
                if match_v_old in vert_outward_vectors:
                    v_new.co += vert_outward_vectors[match_v_old] * self.outward_offset

        if is_entire_island_selected and is_open_sheet:
            bmesh.ops.reverse_faces(bm, faces=sel_faces)
        elif is_open_sheet:
            pass
        else:
            bmesh.ops.delete(bm, geom=sel_faces, context='FACES')

        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.normal_update()
        bmesh.update_edit_mesh(obj.data)
        return {'FINISHED'}

class MESH_OT_omnioutset_edge(bpy.types.Operator):
    """Equidistant outward extrusion for selected edges"""
    bl_idname = "mesh.omnioutset_edge"
    bl_label = "Equidistant Edge Extrude"
    bl_options = {'REGISTER', 'UNDO'}

    outward_offset: bpy.props.FloatProperty(name="Outward Offset", default=0.1, step=0.01)
    local_z_offset: bpy.props.FloatProperty(name="Z Axis Offset", default=0.0, step=0.01)

    @classmethod
    def poll(cls, context):
        return (context.edit_object is not None and 
                context.mode == 'EDIT_MESH' and 
                context.tool_settings.mesh_select_mode[1])

    def execute(self, context):
        obj = context.edit_object
        bm = bmesh.from_edit_mesh(obj.data)

        sel_edges = [e for e in bm.edges if e.select]
        if not sel_edges:
            self.report({'WARNING'}, "Please select boundary edges first!")
            return {'CANCELLED'}

        sel_verts = list(set(v for e in sel_edges for v in e.verts))
        vert_outward_vectors = {}
        vert_z_vectors = {}
        
        for v in sel_verts:
            connected_sel_edges = [e for e in v.link_edges if e in sel_edges]
            outward_normals = []
            z_normals = []
            for e in connected_sel_edges:
                if not e.link_faces: continue
                face = e.link_faces[0]
                z_normals.append(face.normal)
                for loop in face.loops:
                    if loop.edge == e:
                        vec = (loop.link_loop_next.vert.co - loop.vert.co).normalized()
                        outward_normals.append(vec.cross(face.normal).normalized())
                        break
            
            if len(outward_normals) >= 2:
                n1, n2 = outward_normals[:2]
                bisector = (n1 + n2)
                factor = 1.0 / max(0.01, n1.dot(bisector.normalized())) if bisector.length > 0.0001 else 1.0
                vert_outward_vectors[v] = bisector.normalized() * factor
            elif outward_normals:
                vert_outward_vectors[v] = outward_normals[0]
            
            vert_z_vectors[v] = sum(z_normals, Vector()).normalized() if z_normals else Vector((0,0,1))

        ret = bmesh.ops.extrude_edge_only(bm, edges=sel_edges)
        new_verts = [v for v in ret['geom'] if isinstance(v, bmesh.types.BMVert)]
        
        for v_new in new_verts:
            for e in v_new.link_edges:
                v_old = e.other_vert(v_new)
                if v_old in vert_outward_vectors:
                    v_new.co += vert_outward_vectors[v_old] * self.outward_offset
                    v_new.co += vert_z_vectors[v_old] * self.local_z_offset
                    break

        bmesh.ops.recalc_face_normals(bm, faces=bm.faces)
        bm.normal_update()
        bmesh.update_edit_mesh(obj.data)
        return {'FINISHED'}

def menu_func(self, context):
    select_mode = context.tool_settings.mesh_select_mode
    
    if select_mode[1] or select_mode[2]:
        layout = self.layout
        layout.separator()
        layout.label(text="OmniOutset Tools", icon='SHAPEKEY_DATA')
        
        translate = bpy.app.translations.pgettext_iface
        
        if select_mode[2]:
            layout.operator(MESH_OT_omnioutset_face.bl_idname, text=translate("Smart Face Extrude"))
        if select_mode[1]:
            layout.operator(MESH_OT_omnioutset_edge.bl_idname, text=translate("Equidistant Edge Extrude"))

def register():
    bpy.utils.register_class(MESH_OT_omnioutset_face)
    bpy.utils.register_class(MESH_OT_omnioutset_edge)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)
    bpy.app.translations.register(__name__, translation.translations_dict)

def unregister():
    bpy.app.translations.unregister(__name__)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)
    bpy.utils.unregister_class(MESH_OT_omnioutset_face)
    bpy.utils.unregister_class(MESH_OT_omnioutset_edge)