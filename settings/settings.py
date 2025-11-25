from math import radians
import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
)


def copy_enum_items(source_enum, *args, **kwargs):
    print(source_enum.enum_items)
    return EnumProperty(
        name=source_enum.name,
        description=source_enum.description,
        translation_context=source_enum.translation_context,
        default=source_enum.default
        if kwargs.get("default", None) is None
        else kwargs["default"],
        items=[
            (item.identifier, item.name, item.description, item.icon, item.value)
            for item in source_enum.enum_items
        ],
    )


def copy_bool_property(source_bool, *args, **kwargs):
    return BoolProperty(
        name=source_bool.name,
        description=source_bool.description,
        translation_context=source_bool.translation_context,
        default=source_bool.default
        if kwargs.get("default", None) is None
        else kwargs["default"],
    )


def copy_int_property(source_int, *args, **kwargs):
    return IntProperty(
        name=source_int.name,
        description=source_int.description,
        translation_context=source_int.translation_context,
        default=source_int.default
        if kwargs.get("default", None) is None
        else kwargs["default"],
        min=source_int.hard_min,
        max=source_int.hard_max,
        soft_max=source_int.soft_max,
        soft_min=source_int.soft_min,
        step=source_int.step,
        subtype=source_int.subtype,
    )


def copy_float_property(source_float, *args, **kwargs):
    return FloatProperty(
        name=source_float.name,
        description=source_float.description,
        translation_context=source_float.translation_context,
        default=source_float.default
        if kwargs.get("default", None) is None
        else kwargs["default"],
        min=source_float.hard_min,
        max=source_float.hard_max,
        soft_max=source_float.soft_max,
        soft_min=source_float.soft_min,
        subtype=source_float.subtype,
    )


class IMG2BrushSettings(bpy.types.PropertyGroup):
    make_fake_user: BoolProperty(
        name="Make Texture Fake User",
        description="Set each imported texture to have a fake user",
        default=True,
    )

    brush_type: copy_enum_items(
        bpy.types.Brush.bl_rna.properties["stroke_method"], default="ANCHORED"
    )

    brush_spacing: copy_int_property(bpy.types.Brush.bl_rna.properties["spacing"])

    brush_name: StringProperty(
        name="Brush Name",
        description="Name for the created brushes",
        default="Brush",
    )
    brush_numbering: EnumProperty(
        name="Brush Numbering",
        description="Numbering style for multiple brushes",
        items=[
            ("ORIGINAL", "Original", "Original file names"),
            (
                "NO_ZEROES",
                "No Zeroes: X, XX, XXX",
                "Sequential Naming without leading zeros",
            ),
            (
                "ONE_ZERO",
                "One Zero: 0X, XX, XXX",
                "Sequential Naming with 1 leading zero (Default)",
            ),
            (
                "TWO_ZEROES",
                "Two Zeroes: 00X, 0XX, XXX",
                "Sequential Naming with 2 leading zeros",
            ),
        ],
        default="ONE_ZERO",
    )
    
    brush_force_previews: BoolProperty(
        name="Force Generate Brush Texture Previews",
        description="Force generation of brush texture previews after creation",
        default=True,
    )
    
    brush_numbering_suffix: BoolProperty(
        name="Numbering Location",
        description="Add numbering as suffix or prefix",
        default=True,
    )

    brush_separator: StringProperty(
        name="Separator",
        description="Separator between name and number",
        default=" ",
    )

    create_brush_assets: BoolProperty(
        name="Create Brush Assets",
        description="Create brush assets for easier reuse",
        default=True,
    )

    brushes_path: StringProperty(
        name="Brushes Asset Path",
        description="Path to save brush assets",
        default="Brushes",
        maxlen=255,
    )
    brushes_curve: copy_enum_items(
        bpy.types.Brush.bl_rna.properties["curve_distance_falloff_preset"], default="SMOOTH"
    )
    brushes_size: copy_int_property(bpy.types.Brush.bl_rna.properties["size"])

    brushes_sculpt_type: copy_enum_items(
        bpy.types.Brush.bl_rna.properties["sculpt_brush_type"]
    )
    brushes_strength: copy_float_property(bpy.types.Brush.bl_rna.properties["strength"])

    brushes_direction: copy_enum_items(bpy.types.Brush.bl_rna.properties["direction"])

    brushes_rake: copy_bool_property(
        bpy.types.BrushTextureSlot.bl_rna.properties["use_rake"]
    )
    brushes_accumulate: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_accumulate"]
    )
    brushes_frontface: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_frontface"]
    )
    brushes_rotation_angle: copy_float_property(
        bpy.types.BrushTextureSlot.bl_rna.properties["angle"]
    )
    brushes_random_rotation: copy_bool_property(
        bpy.types.BrushTextureSlot.bl_rna.properties["use_random"]
    )
    brushes_random_rotation_amount: copy_float_property(
        bpy.types.BrushTextureSlot.bl_rna.properties["random_angle"]
    )
    brushes_hardness: copy_float_property(bpy.types.Brush.bl_rna.properties["hardness"])
    
    brushes_autosmooth: copy_float_property(bpy.types.Brush.bl_rna.properties["auto_smooth_factor"])
    
    brushes_autosmooth_pressure: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_inverse_smooth_pressure"]
    )

    brushes_size_pressure: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_pressure_size"]
    )
    brushes_strength_pressure: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_pressure_strength"]
    )
    brushes_hardness_pressure: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_hardness_pressure"]
    )

    brushes_hardness_invert: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["invert_hardness_pressure"]
    )
    
    brushes_normal_radius: copy_float_property(
        bpy.types.Brush.bl_rna.properties["normal_radius_factor"]
    )
    brushes_tilt_strength_factor: copy_float_property(
        bpy.types.Brush.bl_rna.properties["tilt_strength_factor"]
    )
    brushes_vector_displacement: copy_bool_property(
        bpy.types.Brush.bl_rna.properties["use_color_as_displacement"]
    )
    brushes_auto_set_bias: BoolProperty(
        name="Auto Set Brush Texture Bias", 
        description="Automatically set the brush texture bias based on texture pixels",
        default=True,
    )
    brushes_select_brush_on_edit: BoolProperty(
        name="Select Brush on Editor select",
        description="Automatically select the brush when selected in the brush list",
        default=True,
    )
    brushes_select_multiple: BoolProperty(
        name="Select Multiple Brushes",
        description="Allow selection of multiple brushes in the brush list",
        default=True,
    )