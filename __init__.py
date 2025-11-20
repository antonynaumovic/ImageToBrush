import bpy
from bpy.props import (
    CollectionProperty,
)

from .ops.debug_ops import IMG2BrushClearDataOperator, IMG2BrushDebugOperator
from .ops.editor_ops import IMG2BrushDeselectAllOperator, IMG2BrushSelectAllOperator
from .ops.importer_ops import IMG2BrushImporter
from .settings.settings import IMG2BrushSettings
from .ui.debug_panel import IMG2BrushDebugPanel
from .ui.editor_list import IMG2BRUSH_UL_created_brushes
from .ui.editor_panel import EditorIMG2BrushPanel
from .ui.main_panel import IMG2BrushPanel
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


bl_info = {
    "name": "Images to Brushes",
    "author": "Antony Naumovic",
    "version": (0, 0, 0, 1),
    "description": "Create brushes from images",
    "blender": (5, 0, 0),
    "location": "View3D > Sidebar > Brushes",
    "category": "Sculpting",
}


classes = (
    IMG2BrushImporter,
    IMG2BrushPanel,
    IMG2BrushDebugOperator,
    IMG2BrushSelectAllOperator,
    IMG2BrushDeselectAllOperator,
    IMG2BRUSH_UL_created_brushes,
    IMG2BrushSettings,
    BrushHolderClass,
    EditorIMG2BrushPanel,
    IMG2BrushClearDataOperator,
    IMG2BrushDebugPanel,
)


def img2brush_func_import(self, context):
    self.layout.operator(IMG2BrushImporter.bl_idname, text="Images to Brushes")


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
