import bpy
from .panel_mixin import IMG2Brush3DPanel

class EditorIMG2BrushPanel(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates an editor Panel in the 3D Viewport"""

    bl_label = "Editor"
    bl_idname = "VIEW3D_PT_img2brushes_editor"

    @classmethod
    def poll(cls, context):
        return len(bpy.context.scene.created_brushes) > 0

    def draw(self, context):
        layout = self.layout

        layout.template_list(
            "IMG2BRUSH_UL_created_brushes",
            "created_brushes",
            context.scene,
            "created_brushes",
            context.scene,
            "created_brushes_index",
        )

        # col = row.column(align=True)
        # col.operator("img2brush.select_all_created_brushes", text="Select All")
        # col.operator("img2brush.deselect_all_created_brushes", text="Deselect All")

        selected_count = sum(1 for i in context.scene.created_brushes if i.selected)
        box = layout.box()
        row = box.row(align=True)
        row.label(text=f"Selected: {selected_count}", icon="BRUSH_DATA")
        row.operator(
            "img2brush.select_all_created_brushes", text="", icon="CHECKBOX_HLT"
        )
        row.operator(
            "img2brush.deselect_all_created_brushes", text="", icon="CHECKBOX_DEHLT"
        )
        # hint: per-item checkboxes are visible inline in the custom UIList above
