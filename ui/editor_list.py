import bpy


class IMG2BRUSH_UL_created_brushes(bpy.types.UIList):
    """Custom UIList for created brushes showing an inline checkbox."""
    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        #item.brush.asset_data.preview_ensure()
        #item.brush.preview_ensure()
        #print(item.brush.preview)
        settings = bpy.context.scene.img2brush_settings
        if item.brush is None:
            return
        if settings.brush_force_previews and item.brush.texture is not None:
            item.brush.texture.preview_ensure()
        
        if item.brush.texture is not None:
            layout.prop(item, "selected", text=item.brush.name, 
                        icon_value=item.brush.texture.preview.icon_id if item.brush.texture.preview else{k : i for i, k in enumerate(bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items.keys())}["BRUSH_DATA"])

        else:
            layout.prop(item, "selected", text=item.brush.name, icon='BRUSH_DATA')