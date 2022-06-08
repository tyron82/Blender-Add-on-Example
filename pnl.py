import bpy

from bpy.types import Panel


class Example_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Operations"
    bl_category = "Example"

    def draw(self, context):
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.operator("object.apply_all_mods", text="test all")

        col = row.column()
        col.operator("object.cancel_all_mods", text="Cancel all")
