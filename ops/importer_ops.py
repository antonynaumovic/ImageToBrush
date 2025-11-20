import bpy
from bpy.props import (
    CollectionProperty,
    StringProperty,
)
from bpy.types import Operator
from bpy_extras.io_utils import ImportHelper

from ..utils.brushes_utils import create_brushes_from_images


class IMG2BrushImporter(Operator, ImportHelper):
    """Import Images as Brushes"""

    bl_idname = "img2brush.import_images"
    bl_label = "Images to Brushes"

    temp_filters: bool = True

    def draw(self, context):
        layout = self.layout

        # Ensure the file browser shows image filters when first opened
        if self.temp_filters:
            params = context.space_data.params
            params.use_filter = True
            params.use_filter_folder = True
            params.use_filter_image = True
            self.temp_filters = False

        box = layout.box()
        box.label(text="Import Settings")

    files: CollectionProperty(
        type=bpy.types.OperatorFileListElement, options={"HIDDEN", "SKIP_SAVE"}
    )
    directory: StringProperty(
        maxlen=1024, subtype="DIR_PATH", options={"HIDDEN", "SKIP_SAVE"}
    )

    filename_ext = "" + ";".join(bpy.path.extensions_image)

    filter_glob = StringProperty(
        default="*" + ";*".join(bpy.path.extensions_image),
        options={"HIDDEN"},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.

    def invoke(self, context, event):
        wm = context.window_manager
        wm.fileselect_add(self)
        return {"RUNNING_MODAL"}

    def execute(self, context):
        return create_brushes_from_images(
            context,
            [self.directory + f.name for f in self.files],
            bpy.context.scene.img2brush_settings.make_fake_user,
        )
