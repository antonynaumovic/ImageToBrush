import bpy


class IMG2BrushDebugOperator(bpy.types.Operator):
    """Debug Operator for Images to Brushes"""

    bl_idname = "img2brush.debug"
    bl_label = "ImagesToBrushesDebug"

    def execute(self, context):
        print("Debug Operator Executed")
        # try:
        #     bpy.ops.object.mode_set(mode="OBJECT")
        # except:
        #     pass

        # if "IMG2Brush_Preview_Sphere" in bpy.data.objects:
        #     bpy.data.objects.remove(
        #         bpy.data.objects["IMG2Brush_Preview_Sphere"], do_unlink=True
        #     )

        # bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=9)
        # bpy.context.view_layer.objects.active = context.object
        # new_mesh = context.object
        # new_mesh.name = "IMG2Brush_Preview_Sphere"
        # bpy.ops.object.shade_smooth()
        # bpy.ops.object.shape_key_add(from_mix=False)

        return {"FINISHED"}


class IMG2BrushClearDataOperator(bpy.types.Operator):
    """Clear Data Operator for Images to Brushes"""

    bl_idname = "img2brush.clear_data"
    bl_label = "ImagesToBrushesClearData"

    def execute(self, context):
        print("Clear Data Operator Executed")

        for item in context.scene.created_brushes:
            if item.brush is not None:
                if item.brush.texture_slot is not None:
                    if item.brush.texture_slot.texture is not None:
                        texture = item.brush.texture_slot.texture
                        if texture.image is not None:
                            bpy.data.images.remove(texture.image, do_unlink=True)
                        bpy.data.textures.remove(texture, do_unlink=True)
                bpy.data.brushes.remove(item.brush, do_unlink=True)
        context.scene.created_brushes.clear()

        return {"FINISHED"}
