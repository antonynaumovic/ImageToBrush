import bpy

from .panel_mixin import IMG2Brush3DPanel
from ..ops.editor_ops import (
    IMG2BRUSH_OT_select_all_brushes,
    IMG2BRUSH_OT_deselect_all_brushes,
)


class IMG2BRUSH_PT_editor_panel(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates an editor Panel in the 3D Viewport"""

    bl_label = "Editor"
    bl_idname = "IMG2BRUSH_PT_editor_panel"

    def draw_header(self, context):
        self.layout.label(text="", icon="OPTIONS")

    @classmethod
    def poll(cls, context):
        return len(bpy.context.scene.created_brushes) > 0

    def draw(self, context):
        layout = self.layout
        settings = bpy.context.scene.img2brush_settings
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
            IMG2BRUSH_OT_select_all_brushes.bl_idname, text="", icon="CHECKBOX_HLT", depress=selected_count == len(context.scene.created_brushes)
        )
        row.operator(
            IMG2BRUSH_OT_deselect_all_brushes.bl_idname, text="", icon="CHECKBOX_DEHLT"
        )
        row.prop(settings, "brush_force_previews", text="", icon="SEQ_PREVIEW")
        row.prop(settings, "brushes_select_brush_on_edit", text="", icon="UV_SYNC_SELECT")
        row.prop(settings, "brushes_select_multiple", text="", icon="DECORATE_UNLOCKED" if settings.brushes_select_multiple else "DECORATE_LOCKED")

        # hint: per-item checkboxes are visible inline in the custom UIList above
