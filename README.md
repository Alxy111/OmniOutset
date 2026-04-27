# 🚀 OmniOutset V1.1.1

**Smart Face Extrude & Equidistant Edge Outset for Blender**

[![Blender 4.2+](https://img.shields.io/badge/Blender-4.2%2B-orange.svg)](https://www.blender.org/)
[![Version](https://img.shields.io/badge/Version-1.1.1-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-GPL_3.0-blue.svg)]()

Welcome to **OmniOutset**, developed by ZXY! This add-on brings industry-standard **"true equidistant outset"** and a silky-smooth **"interactive modal workflow"** to your Blender hard-surface modeling process. 

Leave behind tedious numeric panels, overlapping faces, and manual topology tweaks, and experience a true "flow state" in modeling.

---

## ✨ Key Features

### 🖱️ Immersive Modal Workflow
Say goodbye to the properties panel! Upon activation, the tool takes over your mouse. Drag to preview extrusion and outset in real-time.
* **Dual-Axis Toggle**: Hold `Ctrl` while dragging to seamlessly switch to adjusting the secondary parameter (Outset / Z-Offset).
* **Precision Tweaking**: Hold `Shift` while dragging to slow down movement for high-precision micro-adjustments.

### 🧠 Smart Topology Detection (Face Mode)
Face extrusion now features advanced adjacent face detection logic:
* **Connected Surfaces**: Automatically deletes bottom faces to create a perfect, clean cavity.
* **Isolated Faces**: Automatically retains and flips the normals of the bottom faces to generate a completely closed shell.

### ⌨️ One-Key Smart Router
No need to memorize multiple hotkeys! With the universal smart shortcut (Default: `Shift + Alt + E`), OmniOutset automatically detects whether you are in **Face Mode** or **Edge Mode** and seamlessly invokes the correct interactive tool.

### 🌐 Global Language Pack
OmniOutset seamlessly integrates with Blender's native UI and fully supports **10 languages** out of the box:
* English, Simplified Chinese (简体中文), Traditional Chinese (繁體中文)
* Japanese (日本語), Korean (한국어)
* Spanish (Español), French (Français), German (Deutsch), Russian (Русский), Portuguese (Português)

---

## 📥 Installation

*Note: OmniOutset is built on the new Extensions system architecture and strictly requires **Blender 4.2 LTS or above**.*

1. Go to the **Releases** section on the right side of this GitHub page.
2. Download the latest `omnioutset_v1.1.1.zip` archive (⚠️ *Please do not download the Source Code zip*).
3. Open Blender, navigate to `Edit` -> `Preferences` -> `Get Extensions`.
4. Click the downward arrow in the top right corner, select `Install from Disk`, and choose the downloaded ZIP file.

---

## ⚙️ Configuration & Usage

### Setup Custom Shortcut
You can easily rebind the universal hotkey to match your muscle memory. 
* Go to `Preferences` -> `Extensions` -> `OmniOutset` -> Expand the **OmniOutset Shortcut Configuration** panel and set your preferred key.

### Quick Start
1. Enter **Edit Mode** on any mesh.
2. Select target **Faces** (for Smart Cavity/Shell) OR **Boundary Edges** (for Equidistant Outset).
3. Press `Shift + Alt + E` (or your custom shortcut).
4. Move your mouse to interact, watch the status bar for real-time data, and `Left Click` to confirm!

---

## 🛠️ Bug Reports & Feedback
If you encounter any issues, unit scaling bugs, or have feature requests for future updates, feel free to open an issue on the [Issues](https://github.com/Alxy111/omnioutset/issues) page!
