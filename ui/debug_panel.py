import bpy

from ..ops.debug_ops import IMG2BRUSH_OT_clear_data, IMG2BRUSH_OT_debug
from ..ui.panel_mixin import IMG2Brush3DPanel


class IMG2BRUSH_PT_debug_panel(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "Debug"
    bl_idname = "IMG2BRUSH_PT_debug_panel"
    @classmethod
    def poll(cls, context):
        return bpy.context.preferences.experimental.use_extensions_debug

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.column()
        row.operator(
            IMG2BRUSH_OT_debug.bl_idname,
            text="Debug Operator",
            icon="ERROR",
        )
        row.operator(
            IMG2BRUSH_OT_clear_data.bl_idname,
            text="Clear Data",
            icon="TRASH",
        )
