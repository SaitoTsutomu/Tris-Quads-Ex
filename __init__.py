import bpy

bl_info = {
    "name": "Tris to Quads Ex",  # プラグイン名
    "author": "tsutomu",  # 制作者名
    "version": (1, 0),  # バージョン
    "blender": (3, 1, 0),  # 動作可能なBlenderバージョン
    "support": "COMMUNITY",  # サポートレベル
    "category": "Mesh",  # カテゴリ名
    "description": "Tris to quads by mathematical optimization.",  # 説明文
    "location": "Mesh: Tris to Quads Ex",  # 機能の位置付け
    "warning": "",  # 注意点やバグ情報
    "doc_url": "https://github.com/SaitoTsutomu/Tris-Quads-Ex",  # ドキュメントURL
}


class CEF_OT_tris_convert_to_quads_ex(bpy.types.Operator):
    """Tris to Quads"""

    bl_idname = "object.tris_convert_to_quads_ex"
    bl_label = "Tris to Quads Ex"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        return {"FINISHED"}


ui_classes = (CEF_OT_tris_convert_to_quads_ex,)


def menu_func(self, context):
    self.layout.operator(CEF_OT_tris_convert_to_quads_ex.bl_idname)


def register():
    for ui_class in ui_classes:
        bpy.utils.register_class(ui_class)
    # Adds the new operator to an existing menu(Face in Edit mode).
    bpy.types.VIEW3D_MT_edit_mesh_faces.append(menu_func)


def unregister():
    for ui_class in ui_classes:
        bpy.utils.unregister_class(ui_class)


if __name__ == "__main__":
    register()
