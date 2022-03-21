## Blender Add-on: Tris-Quads-Ex

Using mathematical optimization, tris to quads.

## Installation

- Download https://github.com/SaitoTsutomu/Tris-Quads-Ex/archive/refs/heads/main.zip
- Start Blender.
- Edit menu -> Preferences
  - Select the "Add-ons" tab.
  - Press the "Install ...".
  - Select the downloaded ZIP file and press the button "Install Add-on".
  - Check the "Mesh: Tris to Quads Ex".

### install PuLP

This add-on needs [PuLP](https://github.com/coin-or/pulp).

- on macOS

```
/Applications/Blender.app/Contents/Resources/3.1/python/bin/python3.10 -m pip install pulp
```

- on Windows

```
"C:\Program Files\Blender Foundation\Blender 3.1\3.1\python\bin\python" -m pip install pulp
```

## Usage

- Select an object.
- Turn to the edit mode.
- Select the edges.
- Select "Tris to Quads Ex" of the face menu.

Triangular faces are converted to square faces as possible.

## Introductory Article

- [Blenderで可能な限り三角面を四角面に変換する（数理最適化）](https://qiita.com/SaitoTsutomu/items/b608c80d70a54718ec78)
