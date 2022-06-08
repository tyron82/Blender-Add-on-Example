from . pnl import Example_PT_Panel
from . op import Example_OT_Apply_All_Op, Example_OT_Cancel_All_Op
import bpy
bl_info = {
    "name": "Add-on Example",
    "author": "Default Cube",
    "description": "",
    "blender": (3, 2, 0),
    "version": (0, 0, 2),
    "location": "View3D",
    "warning": "",
    "category": "Object"
}


classes = (Example_OT_Apply_All_Op, Example_OT_Cancel_All_Op, Example_PT_Panel)


def register():
    for c in classes:
        bpy.utils.register_class(c)


def unregister():
    for c in classes:
        bpy.utils.unregister_class(c)
