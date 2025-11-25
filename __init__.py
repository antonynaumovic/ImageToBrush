import bpy
from bpy.props import (
    CollectionProperty,
)

from .ops.debug_ops import IMG2BRUSH_OT_clear_data, IMG2BRUSH_OT_debug
from .ops.editor_ops import (
    IMG2BRUSH_OT_deselect_all_brushes,
    IMG2BRUSH_OT_select_all_brushes,
    IMG2BRUSH_OT_select_brushes,
)
from .ops.importer_ops import IMG2BRUSH_OT_import_brushes
from .settings.settings import IMG2BrushSettings
from .ui.debug_panel import IMG2BRUSH_PT_debug_panel
from .ui.editor_list import IMG2BRUSH_UL_created_brushes
from .ui.editor_panel import IMG2BRUSH_PT_editor_panel
from .ui.main_panel import (
    IMG2BRUSH_PT_panel_action,
    IMG2BRUSH_PT_panel_brush,
    IMG2BRUSH_PT_panel_import,
    IMG2BRUSH_PT_panel_main,
    IMG2BRUSH_PT_panel_naming,
)
from .utils.brush_holder_utils import BrushHolderClass

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


classes = (
    IMG2BRUSH_OT_import_brushes,
    IMG2BRUSH_PT_panel_main,
    IMG2BRUSH_PT_panel_brush,
    IMG2BRUSH_PT_panel_naming,
    IMG2BRUSH_PT_panel_import,
    IMG2BRUSH_PT_panel_action,
    IMG2BRUSH_OT_debug,
    IMG2BRUSH_OT_select_all_brushes,
    IMG2BRUSH_OT_deselect_all_brushes,
    IMG2BRUSH_OT_select_brushes,
    IMG2BRUSH_UL_created_brushes,
    IMG2BrushSettings,
    BrushHolderClass,
    IMG2BRUSH_PT_editor_panel,
    IMG2BRUSH_OT_clear_data,
    IMG2BRUSH_PT_debug_panel,
)


def img2brush_func_import(self, context):
    self.layout.operator(
        IMG2BRUSH_OT_import_brushes.bl_idname, text="Images to Brushes"
    )


def register():
    if bpy.context.preferences.experimental.use_extensions_debug:
        print("Registering Images to Brushes Add-on with Debugging")
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_file_import.append(img2brush_func_import)
    bpy.types.Scene.img2brush_settings = bpy.props.PointerProperty(
        type=IMG2BrushSettings
    )
    bpy.types.Scene.created_brushes = CollectionProperty(
        name="Created Brushes",
        type=BrushHolderClass,
        description="Collection of created brushes",
    )
    bpy.types.Scene.created_brushes_index = bpy.props.IntProperty()


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    bpy.types.TOPBAR_MT_file_import.remove(img2brush_func_import)
    del bpy.types.Scene.img2brush_settings
    del bpy.types.Scene.created_brushes
    del bpy.types.Scene.created_brushes_index


if __name__ == "__main__":
    register()
