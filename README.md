# 🚀 OmniOutset V1.1.0- Smart Face Extrude & Equidistant Edge Outset

Welcome to OmniOutset, developed by ZXY! This add-on is designed to bring industry-standard "true equidistant outset" and a "silky-smooth interactive experience" to your Blender modeling workflow, completely leaving behind tedious numeric panels, overlapping faces, and manual topology tweaks.

---

## 🎉 Latest Version v1.1.0: Immersive Interaction Upgrade

This update completely refactors the underlying logic, bringing an ultimate "flow-state" experience comparable to commercial-grade addons:

* **🖱️ Interactive Modal Workflow**
  Say goodbye to numeric panels! The tool now takes over mouse control upon activation, allowing you to drag and preview extrusion and outset in real time.
  * **Basic Drag**: Directly control the extrusion thickness or outset distance.
  * **Dual-Axis Toggle**: Hold `Ctrl` while dragging to seamlessly switch to adjusting the secondary parameter.
  * **Precision Tweaking**: Hold `Shift` while dragging to slow down the movement for high-precision adjustments.

* **🧠 Smart Topology Detection**
  Face extrusion now features adjacent face detection logic: when extruding connected surfaces, it automatically deletes the bottom faces to create a perfect cavity; when extruding isolated faces, it automatically retains and flips the normals of the bottom faces to generate a complete closed shell.

* **⌨️ Smart Call Shortcut**
  No need to memorize multiple hotkeys! With the default shortcut `Shift + Alt + E`, the add-on automatically detects whether you are in "Face Mode" or "Edge Mode" and seamlessly invokes the corresponding interactive tool.

* **⚙️ Custom Shortcut Preferences**
  Added a visual keymap configuration panel in Blender Preferences (`Extensions` -> `OmniOutset`), allowing you to easily rebind the shortcut to your preferred keys.

---

## 🖥️ Compatibility
Fully compatible and optimized for **Blender 4.2 and above** (Developed entirely on the new Extensions system architecture. Versions below 4.2 are not supported).

## 📥 Installation Guide
1. Download the latest `.zip` archive from the **Releases** section on the right side of this page (Note: Please do not download the source code zip directly).
2. Open Blender, navigate to `Edit` -> `Preferences` -> `Get Extensions`.
3. Click the downward arrow in the top right corner, select `Install from Disk`, and choose the downloaded ZIP file.

💡 *If you encounter any bugs or have feature requests, feel free to let us know on the Issues page!*
