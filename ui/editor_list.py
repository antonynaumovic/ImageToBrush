import bpy

class IMG2BRUSH_UL_created_brushes(bpy.types.UIList):
    """Custom UIList for created brushes showing an inline checkbox."""

    # Draw each item: checkbox + name (+ icon if brush available)
    def draw_item(
        self, context, layout, data, item, icon, active_data, active_propname, index
    ):
        if self.layout_type in {"DEFAULT", "COMPACT"}:
            layout.row().prop(item, "selected", text=item.brush.name)
            split = layout.split(factor=0.01)
            print(item.brush.name)
            col_label = split.column()
            if item.brush is not None:
                col_label.prop(item.brush, "name", icon="BRUSH_DATA")
        elif self.layout_type == "GRID":
            layout.alignment = "CENTER"
            layout.label(text="a", icon="BRUSH_DATA")
