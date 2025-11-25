import bpy

from ..utils.brush_holder_utils import BrushHolderClass


class IMG2BRUSH_OT_select_all_brushes(bpy.types.Operator):
    """Select all created brushes in the scene list"""

    bl_idname = "img2brush.select_all_brushes"
    bl_label = "Select All Created Brushes"

    def execute(self, context):
        for item in context.scene.created_brushes:
            item.selected = True
        return {"FINISHED"}


class IMG2BRUSH_OT_deselect_all_brushes(bpy.types.Operator):
    """Deselect all created brushes in the scene list"""

    bl_idname = "img2brush.deselect_all_brushes"
    bl_label = "Deselect All Created Brushes"

    def execute(self, context):
        for item in context.scene.created_brushes:
            item.selected = False
        return {"FINISHED"}


class IMG2BRUSH_OT_select_brushes(bpy.types.Operator):
    """Select data of selected brushes in the scene list"""

    bl_idname = "img2brush.select_brushes"
    bl_label = "Select Data of Selected Brushes"
    brush_index: bpy.props.IntProperty()

    def invoke(self, context, event):
        ev = []
        if event.ctrl:
            ev.append("Ctrl")
        if event.shift:
            ev.append("Shift")
        if event.alt:
            ev.append("Alt")
        if event.oskey:
            ev.append("OS")
        ev.append("Click")
        print(context.active_operator)
        print("Event modifiers: " + "+".join(ev))

        brushes = context.scene.created_brushes
        if 0 <= self.brush_index < len(brushes):
            brush_item = brushes[self.brush_index]
            self.report({'INFO'}, f"Selected brush: {brush_item.brush.name}")
            brush_item.selected = not brush_item.selected
            if event.shift:
                print(f"Shift-clicked brush: {brush_item.brush.name}")
        else:
            self.report({'WARNING'}, "Invalid brush index")

        self.report({'INFO'}, "+".join(ev))
        return {'FINISHED'}