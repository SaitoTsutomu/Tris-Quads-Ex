import bmesh
import bpy
from pulp import PULP_CBC_CMD, LpMaximize, LpProblem, LpVariable, lpSum, value

bl_info = {
    "name": "Tris to Quads Ex",  # プラグイン名
    "author": "tsutomu",  # 制作者名
    "version": (1, 1),  # バージョン
    "blender": (3, 6, 0),  # 動作可能なBlenderバージョン
    "support": "TESTING",  # サポートレベル
    "category": "Mesh",  # カテゴリ名
    "description": "Tris to quads by mathematical optimization.",  # 説明文
    "location": "Editmode > Face",  # 場所
    "warning": "",  # 注意点やバグ情報
    "doc_url": "https://github.com/SaitoTsutomu/Tris-Quads-Ex",  # ドキュメントURL
}


class CEF_OT_tris_convert_to_quads_ex(bpy.types.Operator):
    """Tris to Quads"""

    bl_idname = "object.tris_convert_to_quads_ex"
    bl_label = "Tris to Quads Ex"
    bl_description = "Tris to quads."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if len(bpy.context.selected_objects) != 1:
            self.report({"WARNING"}, f"Select one object.")
            return {"CANCELLED"}
        # BMesh（bm）が使い回されないようにモードを切り替える
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.mode_set(mode="EDIT")
        obj = bpy.context.edit_object
        bm = bmesh.from_edit_mesh(obj.data)
        bm.edges.ensure_lookup_table()

        m = LpProblem(sense=LpMaximize)
        edges = {}
        for edge in bm.edges:
            if (
                not edge.select
                or len(edge.link_faces) != 2
                or not edge.link_faces[0].select
                or not edge.link_faces[1].select
                or len(edge.link_faces[0].edges) != 3
                or len(edge.link_faces[1].edges) != 3
            ):
                continue
            ln = edge.calc_length()
            edges[edge] = LpVariable(f"v{len(edges):03}", cat="Binary"), ln
        mx = max([i[1] for i in edges.values()], default=1)
        m.setObjective(lpSum(v * (1 + 0.1 * ln / mx) for edge, (v, ln) in edges.items()))
        for face in bm.faces:
            if len(face.edges) != 3:
                continue
            vv = [vln[0] for edge in face.edges if (vln := edges.get(edge)) is not None]
            if len(vv) > 1:
                m += lpSum(vv) <= 1
        solver = PULP_CBC_CMD(gapRel=0.01, timeLimit=60, msg=False)
        m.solve(solver)
        if m.status != 1:
            self.report({"INFO"}, f"{obj.name}: Not solved.")
        else:
            bpy.ops.mesh.select_all(action="DESELECT")
            n = 0
            for edge, (v, _) in edges.items():
                if value(v) > 0.5:
                    edge.select_set(True)
                    n += 1
            self.report({"INFO"}, f"{obj.name}: {n} edges are dissolved.")
            bpy.ops.mesh.dissolve_edges(use_verts=False)
        bm.free()
        del bm
        bpy.ops.mesh.select_all(action="DESELECT")
        bpy.ops.mesh.select_face_by_sides(type="NOTEQUAL")
        bpy.ops.object.mode_set(mode="OBJECT")
        bpy.ops.object.mode_set(mode="EDIT")
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
    bpy.types.VIEW3D_MT_edit_mesh_faces.remove(menu_func)
    for ui_class in ui_classes:
        bpy.utils.unregister_class(ui_class)
