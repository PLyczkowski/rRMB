# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "rRMB Menu",
    "author": "Paweł Łyczkowski",
    "version": (0.2),
    "blender": (2, 70, 0),
    "location": "View3D > RMB",
    "description": "Adds an RMB menu.",
    "warning": "",
    "wiki_url": "",
    "category": "3D View"}

import bpy

class rRMB(bpy.types.Menu):
    bl_label = ""
    bl_idname = "VIEW3D_MT_rRMB"

    def draw(self, context):
        
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object
        layout = self.layout
        
        #Menus in All Modes
        
        layout.operator("view3d.cursor3d", text="Place 3d Cursor", icon="CURSOR")
        #layout.operator("view3d.rcursor3d", text="Place 3d Cursor", icon="CURSOR")
        layout.menu("VIEW3D_MT_rmovecursor")

        layout.operator_menu_enum("object.mode_set", "mode", text="Change Mode")
        
        
        #Mode Specific Menus
        
        if edit_object:
            
            #Edit Mode
            
            if edit_object.type.lower() == "mesh":
                
                #Mesh

#Element Select Options. (Used too often to be in a menu.)
#                layout.separator()
#
#                layout.operator("mesh.select_mode", text="Select Vertices", icon="VERTEXSEL").type="VERT"
#                layout.operator("mesh.select_mode", text="Select Edges", icon="EDGESEL").type="EDGE"
#                layout.operator("mesh.select_mode", text="Select Faces", icon="FACESEL").type="FACE"

                layout.separator()
    
                layout.menu("VIEW3D_MT_edit_mesh_vertices")
                layout.menu("VIEW3D_MT_edit_mesh_edges")
                layout.menu("VIEW3D_MT_edit_mesh_faces")
                
                layout.menu("VIEW3D_MT_edit_mesh_specials")
                
                layout.menu("VIEW3D_MT_edit_mesh_delete")
                
                layout.separator()

                layout.menu("VIEW3D_MT_edit_mesh_showhide")
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_edit_mesh_normals")
                layout.menu("VIEW3D_MT_edit_mesh_clean")
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_uv_map", text="Unwrap")
                
                #layout.separator()
                
                #layout.operator("object.editmode_toggle", text="Exit Edit Mode")
                
            elif edit_object.type.lower() == "armature":
                
                #Armature
                
                arm = edit_object.data
                
                layout.separator()

                layout.menu("VIEW3D_MT_rarmature_transform")

                layout.separator()

                layout.operator("armature.extrude_move")

                if arm.use_mirror_x:
                    layout.operator("armature.extrude_forked")

                layout.operator("armature.duplicate_move")
                layout.operator("armature.merge")
                layout.operator("armature.fill")
                layout.operator("armature.delete")
                layout.operator("armature.split")
                layout.operator("armature.separate")

                layout.separator()

                layout.operator("armature.subdivide", text="Subdivide")
                layout.operator("armature.switch_direction", text="Switch Direction")

                layout.separator()

                layout.menu("VIEW3D_MT_rarmature_autoname")

                layout.separator()

                layout.operator_context = 'INVOKE_DEFAULT'
                layout.operator("armature.armature_layers")
                layout.operator("armature.bone_layers")

                layout.separator()

                layout.menu("VIEW3D_MT_edit_armature_parent")

                #layout.separator()

                #layout.menu("VIEW3D_MT_bone_options_toggle", text="Bone Settings")
                
                #layout.separator()
                
                #layout.operator("object.editmode_toggle", text="Exit Edit Mode")
                
            elif edit_object.type.lower() == "curve":
                
                #Curve
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_transform")
                layout.menu("VIEW3D_MT_mirror")
                layout.menu("VIEW3D_MT_snap")

                layout.separator()

                layout.operator("curve.extrude_move")
                layout.operator("curve.duplicate_move")
                layout.operator("curve.split")
                layout.operator("curve.separate")
                layout.operator("curve.make_segment")
                layout.operator("curve.cyclic_toggle")
                layout.operator("curve.delete", text="Delete...")

                layout.separator()

                layout.menu("VIEW3D_MT_edit_curve_ctrlpoints")
                layout.menu("VIEW3D_MT_edit_curve_segments")

                layout.separator()

                layout.prop_menu_enum(toolsettings, "proportional_edit")
                layout.prop_menu_enum(toolsettings, "proportional_edit_falloff")

                layout.separator()

                layout.menu("VIEW3D_MT_edit_curve_showhide")
                
            elif edit_object.type.lower() == "font":
                
                #Font
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_edit_text_chars")

                layout.separator()

                layout.operator("font.style_toggle", text="Toggle Bold").style = 'BOLD'
                layout.operator("font.style_toggle", text="Toggle Italic").style = 'ITALIC'
                layout.operator("font.style_toggle", text="Toggle Underline").style = 'UNDERLINE'
                layout.operator("font.style_toggle", text="Toggle Small Caps").style = 'SMALL_CAPS'

                layout.separator()

                layout.operator("font.insert_lorem")
            
        elif mode_string == 'OBJECT':
            
            #Object Mode with Active Object
            
            if obj:
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_robjecttransform")
                
                #layout.menu("VIEW3D_MT_transform_object")
                #layout.menu("VIEW3D_MT_mirror")
                #layout.menu("VIEW3D_MT_object_clear")
                #layout.menu("VIEW3D_MT_object_apply")
                #layout.menu("VIEW3D_MT_snap")

                layout.separator()

                layout.menu("VIEW3D_MT_object_showhide")
                layout.operator("object.move_to_layer", text="Move to Layer...")
                layout.menu("VIEW3D_MT_object_group")
                layout.menu("VIEW3D_MT_object_parent")
                
                layout.separator()

                #layout.menu("VIEW3D_MT_object_animation")

                #layout.separator()

                layout.operator("object.join")
                layout.operator("object.duplicate_move", text="Duplicate")
                layout.operator("object.duplicate_move_linked")
                layout.operator("object.delete", text="Delete...")
                
                layout.separator()
                
                layout.operator("object.proxy_make", text="Make Proxy...")
                layout.menu("VIEW3D_MT_make_links", text="Make Links...")
                layout.operator("object.make_dupli_face")
                layout.operator_menu_enum("object.make_local", "type", text="Make Local...")
                layout.menu("VIEW3D_MT_make_single_user")
                layout.operator_menu_enum("object.convert", "target")

                layout.separator()
                
                layout.menu("VIEW3D_MT_object_track")
                layout.menu("VIEW3D_MT_object_constraints")
                
                #layout.separator()
                #layout.operator("object.editmode_toggle", text="Enter Edit Mode", icon='EDITMODE_HLT')

                #layout.separator()

                #layout.menu("VIEW3D_MT_object_quick_effects")

                #layout.separator()

                #layout.menu("VIEW3D_MT_object_game")

                #layout.separator()
                
            else:
                
                #Object Mode without Active Object
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_object_showhide")
        
class VIEW3D_MT_rarmature_autoname(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Autoname"

    def draw(self, context):
        
        layout = self.layout
        
        layout.operator_context = 'EXEC_AREA'
        layout.operator("armature.autoside_names", text="AutoName Left/Right").type = 'XAXIS'
        layout.operator("armature.autoside_names", text="AutoName Front/Back").type = 'YAXIS'
        layout.operator("armature.autoside_names", text="AutoName Top/Bottom").type = 'ZAXIS'
        layout.operator("armature.flip_names")
        
class VIEW3D_MT_rarmature_transform(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Transform"

    def draw(self, context):
        
        layout = self.layout
        obj = context.object
        
        # base menu
        layout.operator("transform.translate", text="Grab/Move")
        layout.operator("transform.rotate", text="Rotate")
        layout.operator("transform.resize", text="Scale")
        
        layout.separator()
        
        layout.menu("VIEW3D_MT_rsnap")
        layout.menu("VIEW3D_MT_mirror")
        layout.menu("VIEW3D_MT_edit_armature_roll")

        layout.separator()

        layout.operator("transform.tosphere", text="To Sphere")
        layout.operator("transform.shear", text="Shear")
        layout.operator("transform.bend", text="Bend")
        layout.operator("transform.push_pull", text="Push/Pull")
        layout.operator("object.vertex_warp", text="Warp")
        layout.operator("object.vertex_random", text="Randomize")

        # armature specific
        
        layout.separator()

        if obj.type == 'ARMATURE' and obj.mode in {'EDIT', 'POSE'}:
            if obj.data.draw_type == 'BBONE':
                layout.operator("transform.transform", text="Scale BBone").mode = 'BONE_SIZE'
            elif obj.data.draw_type == 'ENVELOPE':
                layout.operator("transform.transform", text="Scale Envelope Distance").mode = 'BONE_SIZE'
                layout.operator("transform.transform", text="Scale Radius").mode = 'BONE_ENVELOPE'

        if context.edit_object and context.edit_object.type == 'ARMATURE':
            layout.operator("armature.align")
        

class VIEW3D_MT_robjecttransform(bpy.types.Menu):
    bl_context = "objectmode"
    bl_label = "Transform"

    def draw(self, context):
        
        layout = self.layout
        
        layout.operator("transform.translate", text="Grab/Move")
        layout.operator("transform.rotate", text="Rotate")
        layout.operator("transform.resize", text="Scale")
        
        layout.separator()
        
        layout.menu("VIEW3D_MT_mirror")
        layout.menu("VIEW3D_MT_object_clear")
        layout.menu("VIEW3D_MT_object_apply")
        layout.menu("VIEW3D_MT_snap")
        
        layout.separator()
        
        layout.operator_context = 'EXEC_AREA'
        layout.operator("object.origin_set", text="Geometry to Origin").type = 'GEOMETRY_ORIGIN'
        layout.operator("object.origin_set", text="Origin to Geometry").type = 'ORIGIN_GEOMETRY'
        layout.operator("object.origin_set", text="Origin to 3D Cursor").type = 'ORIGIN_CURSOR'
        
        layout.separator()
        
        layout.operator("transform.tosphere", text="To Sphere")
        layout.operator("transform.shear", text="Shear")
        layout.operator("transform.warp", text="Warp")
        layout.operator("transform.push_pull", text="Push/Pull")
        
        if context.edit_object and context.edit_object.type == 'ARMATURE':
            layout.operator("armature.align")
        else:
            layout.operator_context = 'EXEC_REGION_WIN'
            layout.operator("transform.transform", text="Align to Transform Orientation").mode = 'ALIGN' # XXX see alignmenu() in edit.c of b2.4x to get this working
        
        
            
class VIEW3D_MT_rmovecursor(bpy.types.Menu):
    bl_context = "view_3d"
    bl_label = "Move 3d Cursor"

    def draw(self, context):
        
        layout = self.layout
        
        layout.operator("view3d.snap_cursor_to_selected", text="To Selected")
        layout.operator("view3d.snap_cursor_to_center", text="To Center")
        layout.operator("view3d.snap_cursor_to_grid", text="To Grid")
        layout.operator("view3d.snap_cursor_to_active", text="To Active")
        
class VIEW3D_MT_rsnap(bpy.types.Menu):
    bl_context = "view_3d"
    bl_label = "Snap Selected"

    def draw(self, context):
        
        layout = self.layout
        
        layout.operator("view3d.snap_selected_to_grid", text="To Grid")
        layout.operator("view3d.snap_selected_to_cursor", text="To Cursor").use_offset = False
        layout.operator("view3d.snap_selected_to_cursor", text="To Cursor (Offset)").use_offset = True
        
        
class VIEW3D_MT_robject(bpy.types.Menu):
    bl_context = "objectmode"
    bl_label = "Object"

    def draw(self, context):
        
        layout = self.layout
        
#------------------- OPERATORS ------------------------------     

class rPlace3DCursor(bpy.types.Operator):
    
    bl_idname = "view3d.rcursor3d"
    bl_label = "rCursor3D"
    bl_description = "rCursor3D"
    bl_register = True

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        #TODO A way to set the 3d cursor, probably according to provided 2d coordinates.
        #bpy.ops.view3d.cursor3d()
        
        return {'FINISHED'}
        
#------------------- REGISTER ------------------------------     

addon_keymaps = []

def register():
    
    bpy.utils.register_module(__name__)
    
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
        kmi = km.keymap_items.new('wm.call_menu', 'ACTIONMOUSE', 'PRESS')
        kmi.properties.name = "VIEW3D_MT_rRMB"
        addon_keymaps.append((km, kmi))
        kmi = km.keymap_items.new('view3d.cursor3d', 'ACTIONMOUSE', 'PRESS', alt=True)
        addon_keymaps.append((km, kmi))

def unregister():
    
    bpy.utils.unregister_module(__name__)
    
    wm = bpy.context.window_manager
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
        
if __name__ == "__main__":
    register()
    






