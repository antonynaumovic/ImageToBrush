import bpy

from ..ops.importer_ops import IMG2BRUSH_OT_import_brushes
from ..utils.brushes_utils import create_brush_name
from .panel_mixin import IMG2Brush3DPanel


class IMG2BRUSH_PT_panel_main(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""

    bl_label = "Images to Brushes"
    bl_idname = "IMG2BRUSH_PT_panel_main"
    
    def draw_header(self, context):
        self.layout.label(text="", icon="FILE_IMAGE")

    def draw(self, context):
        layout = self.layout

class IMG2BRUSH_PT_panel_naming(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_parent_id = IMG2BRUSH_PT_panel_main.bl_idname
    bl_label = "Brush Naming"
    bl_idname = "IMG2BRUSH_PT_panel_naming"
    
    def draw_header(self, context):
        self.layout.label(text="", icon="OUTLINER_OB_FONT")
    
    
    def draw(self, context):
        layout = self.layout
        settings = bpy.context.scene.img2brush_settings
        box = layout.box()
        row = box.column()
        row.label(text="Naming Convention:")
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
        
class IMG2BRUSH_PT_panel_brush(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_parent_id = IMG2BRUSH_PT_panel_main.bl_idname
    bl_label = "Brush Settings"
    bl_idname = "IMG2BRUSH_PT_panel_brush"
    
    def draw_header(self, context):
        self.layout.label(text="", icon="BRUSH_DATA")
    
    def draw(self, context):
        layout = self.layout
        settings = bpy.context.scene.img2brush_settings
        box = layout.box()
        row = box.column(align=True)
        row.prop(settings, "brush_type", icon="BRUSH_DATA", text="Stroke Method")

        if settings.brush_type in {"LINE", "CURVE", "SPACE"}:
            box.row().prop(settings, "brush_spacing", icon="BRUSH_DATA")

        box.row().prop(settings, "brushes_curve", text="Falloff")
        
        box.row().prop(settings, "brushes_sculpt_type")
        
        row = box.row(align=True)
        row.prop(settings, "brushes_size", text="Size", slider=True)
        row.prop(settings, "brushes_size_pressure", icon="STYLUS_PRESSURE", icon_only=True)
        
        row = box.row(align=True)
        row.prop(settings, "brushes_strength")
        row.prop(settings, "brushes_strength_pressure", icon="STYLUS_PRESSURE", icon_only=True)
        
        row = box.row(align=True)
        row.prop(settings, "brushes_direction", expand=True, text="Direction:")
        
        
        box.row().prop(settings, "brushes_normal_radius", text="Normal Radius")
        box.row().prop(settings, "brushes_tilt_strength_factor", text="Tilt Strength")
        
        row = box.row(align=True)
        row.prop(settings, "brushes_hardness", text="Hardness")
        row.prop(settings, "brushes_hardness_invert", icon="ARROW_LEFTRIGHT", icon_only=True)
        row.prop(settings, "brushes_hardness_pressure", icon="STYLUS_PRESSURE", icon_only=True)
        
        row = box.row(align=True)
        row.prop(settings, "brushes_autosmooth", text="Auto Smooth")
        row.prop(settings, "brushes_autosmooth_pressure", icon="STYLUS_PRESSURE", icon_only=True)
        
        box.row().prop(settings, "brushes_rotation_angle")
        
        grid = box.column_flow(align=True )
        grid.prop(settings, "brushes_rake")
        
        grid.prop(settings, "brushes_accumulate")
        
        grid.prop(settings, "brushes_frontface")
        
        grid.prop(settings, "brushes_vector_displacement")
        
        row = grid.row()
        row.prop(settings, "brushes_random_rotation", text="Random Rotation")
        row.prop(settings, "brushes_random_rotation_amount") if settings.brushes_random_rotation else None
        
        box.row().prop(settings, "brushes_auto_set_bias", text="Auto Set Texture Bias")
        
        

class IMG2BRUSH_PT_panel_import(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_parent_id = IMG2BRUSH_PT_panel_main.bl_idname
    bl_label = "Import Settings"
    bl_idname = "IMG2BRUSH_PT_panel_import"
    
    def draw_header(self, context):
        self.layout.label(text="", icon="IMPORT")
    
    def draw(self, context):
        layout = self.layout
        settings = bpy.context.scene.img2brush_settings
        box = layout.box()
        # row = box.column(align=True)
        # row.prop(settings, "create_brush_assets", icon="ASSET_MANAGER")

        if settings.create_brush_assets:
            row = box.column(heading="Brushes Asset Path:")
            row.prop(settings, "brushes_path", icon="CURRENT_FILE", text="")
            
class IMG2BRUSH_PT_panel_action(IMG2Brush3DPanel, bpy.types.Panel):
    """Creates a Panel in the Object properties window"""
    bl_parent_id = IMG2BRUSH_PT_panel_main.bl_idname
    bl_label = ""
    bl_idname = "IMG2BRUSH_PT_panel_action"
    
    bl_options = {"HIDE_HEADER"}

            
    def draw(self, context):
        layout = self.layout
        settings = bpy.context.scene.img2brush_settings
        canContinue = True
        if not bpy.data.is_saved and settings.create_brush_assets:
            canContinue = False


    

        row = layout.row(align=True)
        row.alert = not canContinue
        row.operator(IMG2BRUSH_OT_import_brushes.bl_idname, text="Images to Brushes")
        row.prop(
            settings,
            "make_fake_user",
            icon_only=True,
            icon="FAKE_USER_ON" if settings.make_fake_user else "FAKE_USER_OFF",
        )
        row.enabled = canContinue