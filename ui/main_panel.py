import bpy

from ..ops.importer_ops import IMG2BrushImporter
from ..utils.brushes_utils import create_brush_name
from .panel_mixin import IMG2Brush3DPanel


class IMG2BrushPanel(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "Images to Brushes"
    bl_idname = "OBJECT_PT_img2brushes_main"

    def draw(self, context):
        layout = self.layout
        settings = bpy.context.scene.img2brush_settings

        canContinue = True
        if not bpy.data.is_saved and settings.create_brush_assets:
            canContinue = False

        box = layout.box()
        row = box.row(heading="Brush Settings")
        row.label(text="Brush Settings", icon="BRUSH_DATA")

        row = box.column()
        row.label(text="Brush Naming:")
        row.prop(settings, "brush_numbering", icon="SORTALPHA", text="")

        if settings.brush_numbering != "ORIGINAL":
            row = box.column(heading="Brush Name")
            row.label(text="Name:")

            row = box.row(align=True)
            row.prop(
                settings,
                "brush_name",
                icon="FONT_DATA",
                text="",
                placeholder="Brush Name",
            )
            row.prop(
                settings,
                "brush_numbering_suffix",
                icon_only=True,
                icon="BACK" if settings.brush_numbering_suffix else "FORWARD",
            )

            row = box.column()
            row.label(text="Separator:")
            row.prop(
                settings,
                "brush_separator",
                icon="SORTBYEXT",
                text="",
                placeholder="Separator",
            )

        main_name_preview = (
            settings.brush_name
            if settings.brush_numbering != "ORIGINAL"
            else "Filename"
        )

        row = box.column()
        row.label(text="Preview: {r}".format(r=create_brush_name(main_name_preview, 0)))
        row.enabled = False

        row = box.column()
        row.separator(type="LINE", factor=0.2)
        row.scale_x = 1.0

        row = box.column(align=True)
        row.label(text="Brush Type:")
        row.prop(settings, "brush_type", icon="BRUSH_DATA", text="")

        if settings.brush_type in {"LINE", "CURVE", "SPACE"}:
            row = box.row()
            row.prop(settings, "brush_spacing", icon="BRUSH_DATA")

        row = box.row()
        row.prop(settings, "brushes_curve")

        box = layout.box()
        row = box.row()
        row.label(text="Import Settings", icon="IMPORT")
        row = box.column(align=True)
        row.prop(settings, "create_brush_assets", icon="ASSET_MANAGER")

        if settings.create_brush_assets:
            row = box.column(heading="Brushes Asset Path:")
            row.prop(settings, "brushes_path", icon="CURRENT_FILE", text="")

        row = layout.row(align=True)
        row.alert = not canContinue
        row.operator(IMG2BrushImporter.bl_idname, text="Images to Brushes")
        row.prop(
            settings,
            "make_fake_user",
            icon_only=True,
            icon="FAKE_USER_ON" if settings.make_fake_user else "FAKE_USER_OFF",
        )
        row.enabled = canContinue
