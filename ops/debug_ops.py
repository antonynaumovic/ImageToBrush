import time
import bpy
import mathutils
import bpy_extras.view3d_utils
from mathutils import Vector
import math


def context_override():
    for window in bpy.context.window_manager.windows:
        screen = window.screen
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for region in area.regions:
                    if region.type == 'WINDOW':
                        return {'window': window, 'screen': screen, 'area': area, 'region': region, 'scene': bpy.context.scene}

class IMG2BRUSH_OT_debug(bpy.types.Operator):
    """Debug Operator for Images to Brushes"""

    bl_idname = "img2brush.debug"
    bl_label = "ImagesToBrushesDebug"

    def execute(self, context):
        print("Debug Operator Executed")
        # try:
        #     bpy.ops.object.mode_set(mode="OBJECT")
        # except Exception:
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
        
        # bpy.ops.object.shape_key_add(from_mix=False)
        # new_mesh.select_set(True)
        
        settings = bpy.context.scene.img2brush_settings
        print(settings.brushes_direction)
        
        """
        area = next(iter([area for area in bpy.context.window.screen.areas if area.type == 'VIEW_3D']))
        with bpy.context.temp_override(area=area):
            view3d = bpy.context.space_data
            region = next(iter([i for i in area.regions if i.type == 'WINDOW']))
            rv3d = view3d.region_3d

            #bpy.ops.object.mode_set(mode="OBJECT")
            
            # bpy.ops.view3d.view_axis(type='FRONT')
            #bpy.ops.view3d.view_selected()
            
            view_matrix = mathutils.Matrix.Identity(4)
            view_matrix[0][0] = 1
            view_matrix[1][2] = 1
            view_matrix[2][1] = -1
            view_matrix[3][3] = 1
            rv3d.view_matrix = view_matrix
            
            view_location = mathutils.Vector((0.0, -0.2918, 0.0))
            
            rv3d.view_location = view_location
            
            view_rotation = mathutils.Quaternion((0.7071, 0.7071, 0, 0.0))
            
            rv3d.view_rotation = view_rotation
            
            #bpy.ops.view3d.view_axis(type='FRONT')
            #bpy.ops.view3d.view_selected()
            #bpy.context.view_layer.update()
            
            coordinates = [(0, -1, 0), (0, -1, 0)]  # Points on the mesh surface (assuming sphere at origin)
                    
            matrix = bpy.context.active_object.matrix_world

            mesh = bpy.context.active_object.bound_box

            col0 = matrix.col[0]
            col1 = matrix.col[1]
            col2 = matrix.col[2]
            col3 = matrix.col[3]

            minX = 1
            maxX = 0
            minY = 1
            maxY = 0

            numVertices = len(mesh)
            
            positionsX = []
            positionsY = []

            for t in range(0, numVertices):

                co = mesh[t]

                pos = (col0 * co[0]) + (col1 * co[1]) + (col2 * co[2]) + col3
                
                print ("Vertex "+str(t)+": ("+str(pos.x)+", "+str(pos.y)+", "+str(pos.z)+")")

                pos = bpy_extras.view3d_utils.location_3d_to_region_2d(
                    region,
                    rv3d,
                    pos,
                )
                
                positionsX.append(pos.x)
                positionsY.append(pos.y)
                
                print ("Vertex Screen"+str(t)+": ("+str(pos.x)+", "+str(pos.y)+")")
            
            
            # pMinX = str(int(minX*WIDTH))
            # pMinY = str(int(minY*HEIGHT))
            # pMaxX = str(int(maxX*WIDTH))
            # pMaxY = str(int(maxY*HEIGHT))
            # print("  ("+pMinX+", "+pMinY+") - ("+pMaxX+", "+pMaxY+")")

            print("  ("+str(min(positionsX))+", "+str(min(positionsY))+") - ("+str(max(positionsX))+", "+str(max(positionsY))+")")"""
        """
        bpy.ops.object.mode_set(mode="SCULPT")
        brush = bpy.context.tool_settings.sculpt.brush
        mouse_positions = [(WIDTH/2, HEIGHT/2), (WIDTH/2, HEIGHT/2 +200)]  # Center-ish of viewport
        print(mouse_positions)
        strokes = []
        for i, coordinate in enumerate(coordinates):
            stroke = {
                "name": "stroke",
                "mouse": mouse_positions[i] if i < len(mouse_positions) else (400, 300),
                "mouse_event": mouse_positions[i] if i < len(mouse_positions) else (400, 300),
                "is_start": True if i == 0 else False,
                "location": mathutils.Vector(coordinate),
                "size": 250,
                "pressure": 1.0,
                "time": float(i),
                "x_tilt": 0.0,
                "y_tilt": 0.0,
            }
            print(f"Stroke {i}: {stroke}")
            strokes.append(stroke)
        # If brush is in anchored mode, only send one stroke dict
        if hasattr(brush, 'stroke_method') and brush.stroke_method == 'ANCHOR':
            print("Anchored brush mode detected. Sending single stroke.")
            bpy.ops.sculpt.brush_stroke(stroke=strokes, ignore_background_click=True)
        else:
            print("Normal brush mode. Sending stroke list.")
            bpy.ops.sculpt.brush_stroke(stroke=strokes, mode='NORMAL', ignore_background_click=True)
        """

        return {"FINISHED"}


class IMG2BRUSH_OT_clear_data(bpy.types.Operator):
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
