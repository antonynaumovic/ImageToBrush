import bpy

class BrushHolderClass(bpy.types.PropertyGroup):
    brush: bpy.props.PointerProperty(type=bpy.types.Brush)
    selected: bpy.props.BoolProperty(name="Selected", default=False)
