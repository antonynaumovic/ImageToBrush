import bpy
from ..ui.panel_mixin import IMG2Brush3DPanel
from ..ops.debug_ops import IMG2BrushClearDataOperator, IMG2BrushDebugOperator

class IMG2BrushDebugPanel(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "Debug"
    bl_idname = "OBJECT_PT_img2brushes_debug"
    
    @classmethod
    def poll(cls, context):
        return bpy.context.preferences.experimental.use_extensions_debug

    def draw(self, context):
        layout = self.layout
        box = layout.box()
        row = box.column()
        row.operator(
            IMG2BrushDebugOperator.bl_idname,
            text="Debug Operator",
            icon="ERROR",
        )
        row.operator(
            IMG2BrushClearDataOperator.bl_idname,
            text="Clear Data",
            icon="TRASH",
        )