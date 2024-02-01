bl_info = {
    "name": "Japanese_English_Toggle",
    "blender": (2, 80, 0),
    "category": "Interface",
}

import bpy


class INTERFACE_OT_swap_language(bpy.types.Operator):
    bl_idname = "interface.change_language"
    bl_label = "Swap Languages"
    language_one: bpy.props.StringProperty(default="en_US")
    language_two: bpy.props.StringProperty(default="ja_JP")

    def execute(self, context):
        view = context.preferences.view
        if view.language == self.language_one:
            view.language = self.language_two
        else:
            view.language = self.language_one
        return {'FINISHED'}


def register():
    bpy.utils.register_class(INTERFACE_OT_swap_language)

    wm = bpy.context.window_manager
    kc = wm.keyconfigs.user
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new(INTERFACE_OT_swap_language.bl_idname, type='E', value='PRESS', alt=True)


if __name__ == "__main__":
    register()
