import bpy
from os.path import join

def update_brush_selection(self, context):
    settings = bpy.context.scene.img2brush_settings
    if not settings.brushes_select_multiple:
        if self.selected:
        # Deselect all other brushes
            for item in context.scene.created_brushes:
                if item != self:
                    item.selected = False
                    
        amount_selected = sum(1 for item in context.scene.created_brushes if item.selected)
        if amount_selected == 0:
            self.selected = True  # Ensure at least one is selected
    
    
    if context.active_object.mode == "SCULPT" and self.selected:
        bpy.ops.brush.asset_activate(asset_library_type='LOCAL', relative_asset_identifier=join("Brush", f"{self.brush.name}") )  # Activate the brush in sculpt mode



class BrushHolderClass(bpy.types.PropertyGroup):
    brush: bpy.props.PointerProperty(type=bpy.types.Brush)
    selected: bpy.props.BoolProperty(name="Selected", default=False, update=update_brush_selection)
    image: bpy.props.PointerProperty(type=bpy.types.Image)


