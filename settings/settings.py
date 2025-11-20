import bpy
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    StringProperty,
)


class IMG2BrushSettings(bpy.types.PropertyGroup):
    make_fake_user: BoolProperty(
        name="Make Texture Fake User",
        description="Set each imported texture to have a fake user",
        default=True,
    )

    brush_type: EnumProperty(
        name="Brush Type",
        description="Type of brush to create",
        items=[
            (item.identifier, item.name, item.description)
            for item in bpy.types.Brush.bl_rna.properties["stroke_method"].enum_items
        ],
        default="ANCHORED",
    )

    brush_spacing: IntProperty(
        name="Brush Spacing",
        description="Spacing between brush marks",
        default=10,
        min=1,
        max=500,
    )
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
    brushes_curve: EnumProperty(
        name="Brush Curve",
        description="Curve to use for the brushes",
        items=[
            (item.identifier, item.name, item.description, item.icon, index)
            for index, item in enumerate(
                bpy.types.Brush.bl_rna.properties[
                    "curve_distance_falloff_preset"
                ].enum_items
            )
        ],
        default="SMOOTH",
    )
    brushes_size: IntProperty(
        name="Brush Size",
        description="Size of the brushes",
        default=100,
        min=1,
        max=1000,
    )
    brushes_type: EnumProperty(
        name="Brush Type",
        description="Type of brushes to create",
        items=[
            (item.identifier, item.name, item.description)
            for item in bpy.types.Brush.bl_rna.properties[
                "sculpt_brush_type"
            ].enum_items
        ],
        default="DRAW",
    )
    brushes_strength: FloatProperty(
        name="Brush Strength",
        description="Strength of the brushes",
        default=0.5,
        min=0.0,
        soft_max=1.0,
    )
    brushes_direction: BoolProperty(
        name="Brush Direction",
        description="Add or subtract mode for brushes",
        default=False,
    )
