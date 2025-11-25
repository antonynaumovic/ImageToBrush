class IMG2Brush3DPanel:
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Brushes"
    

    @classmethod
    def poll(cls, context):
        return context is not None
