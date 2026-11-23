## Blender Add-on: Tris-Quads-Ex

Using mathematical optimization, tris to quads.

## Installation

Requires Blender 5.2 or later.

- Download https://github.com/SaitoTsutomu/Tris-Quads-Ex/archive/refs/heads/master.zip
- Start Blender.
- Edit menu -> Preferences
  - Select the "Get Extensions" tab.
  - Open the drop-down menu (v) at the top right and select "Install from Disk...".
  - Select the downloaded ZIP file and press the button "Install from Disk".
  - Make sure "Tris to Quads Ex" is enabled in the "Add-ons" tab.

Note: On Apple Silicon Macs, Rosetta 2 is required because the bundled CBC solver is an x86_64 binary.

## Usage

- Select an object.
- Turn to the edit mode.
- Select the edges.
- Select "Tris to Quads Ex" of the face menu.

Triangular faces are converted to square faces as possible.

## Introductory Article

- [Blenderで可能な限り三角面を四角面に変換する（数理最適化）](https://qiita.com/SaitoTsutomu/items/b608c80d70a54718ec78)
