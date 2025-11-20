import bpy


class IMG2BrushSelectAllOperator(bpy.types.Operator):
    """Select all created brushes in the scene list"""

    bl_idname = "img2brush.select_all_created_brushes"
    bl_label = "Select All Created Brushes"

    def execute(self, context):
        for item in context.scene.created_brushes:
            item.selected = True
        return {"FINISHED"}


class IMG2BrushDeselectAllOperator(bpy.types.Operator):
    """Deselect all created brushes in the scene list"""

    bl_idname = "img2brush.deselect_all_created_brushes"
    bl_label = "Deselect All Created Brushes"

    def execute(self, context):
        for item in context.scene.created_brushes:
            item.selected = False
        return {"FINISHED"}
