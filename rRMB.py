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
    "version": (0.3),
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
                layout.menu("VIEW3D_MT_rsnap")

                layout.separator()

                layout.operator("curve.extrude_move")
                layout.operator("curve.duplicate_move")
                layout.operator("curve.split")
                layout.operator("curve.separate")
                layout.operator("curve.make_segment")
                layout.operator("curve.cyclic_toggle")
                layout.operator("curve.delete", text="Delete")

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
                layout.menu("VIEW3D_MT_robject_apply")
                layout.menu("VIEW3D_MT_robject_clear")
                layout.menu("VIEW3D_MT_rorigintransform")
                
                #layout.menu("VIEW3D_MT_transform_object")
                #layout.menu("VIEW3D_MT_mirror")
                #layout.menu("VIEW3D_MT_object_clear")
                #layout.menu("VIEW3D_MT_object_apply")
                #layout.menu("VIEW3D_MT_snap")

                layout.separator()

                layout.menu("VIEW3D_MT_object_showhide")
                layout.operator("object.move_to_layer", text="Move to Layer")
                layout.menu("VIEW3D_MT_object_group")
                layout.menu("VIEW3D_MT_object_parent")
                
                layout.separator()

                #layout.menu("VIEW3D_MT_object_animation")

                #layout.separator()

                layout.operator("object.join")
                layout.operator("object.duplicate_move", text="Duplicate")
                layout.operator("object.duplicate_move_linked")
                layout.operator("view3d.copybuffer", text="Copy")
                layout.operator("view3d.pastebuffer", text="Paste")
                layout.operator("object.delete", text="Delete")
                
                # layout.separator()
                
                # layout.operator("object.proxy_make", text="Make Proxy...")
                # layout.menu("VIEW3D_MT_make_links", text="Make Links...")
                # layout.operator("object.make_dupli_face")
                # layout.operator_menu_enum("object.make_local", "type", text="Make Local...")
                # layout.menu("VIEW3D_MT_make_single_user")
                # layout.operator_menu_enum("object.convert", "target")

                layout.separator()
                
                layout.menu("VIEW3D_MT_robjectdata")
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
                layout.operator("view3d.pastebuffer", text="Paste")
        
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
        # layout.menu("VIEW3D_MT_object_clear")
        # layout.menu("VIEW3D_MT_object_apply")
        layout.menu("VIEW3D_MT_rsnap")
        layout.operator("object.origin_set", text="Move Geometry to Origin").type = 'GEOMETRY_ORIGIN'
        
        # layout.separator()
        
        # layout.operator_context = 'EXEC_AREA'
        # layout.operator("object.origin_set", text="Geometry to Origin").type = 'GEOMETRY_ORIGIN'
        # layout.operator("object.origin_set", text="Origin to Geometry").type = 'ORIGIN_GEOMETRY'
        # layout.operator("object.origin_set", text="Origin to 3D Cursor").type = 'ORIGIN_CURSOR'
        
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

class VIEW3D_MT_robject_clear(bpy.types.Menu):
    bl_label = "Clear Transforms"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.location_clear", text="Location")
        layout.operator("object.rotation_clear", text="Rotation")
        layout.operator("object.scale_clear", text="Scale")
        layout.operator("object.origin_clear", text="Location Relative To Parent (Origin)")

class VIEW3D_MT_robject_apply(bpy.types.Menu):
    bl_label = "Apply Transforms"

    def draw(self, context):
        layout = self.layout

        # props = layout.operator("object.transform_apply", text="Location", text_ctxt=i18n_contexts.default)
        props = layout.operator("object.transform_apply", text="Location")
        props.location, props.rotation, props.scale = True, False, False

        # props = layout.operator("object.transform_apply", text="Rotation", text_ctxt=i18n_contexts.default)
        props = layout.operator("object.transform_apply", text="Rotation")
        props.location, props.rotation, props.scale = False, True, False

        # props = layout.operator("object.transform_apply", text="Scale", text_ctxt=i18n_contexts.default)
        props = layout.operator("object.transform_apply", text="Scale")
        props.location, props.rotation, props.scale = False, False, True
        # props = layout.operator("object.transform_apply", text="Rotation & Scale", text_ctxt=i18n_contexts.default)
        props = layout.operator("object.transform_apply", text="Rotation & Scale")
        props.location, props.rotation, props.scale = False, True, True

        layout.separator()

        # layout.operator("object.visual_transform_apply", text="Visual Transform", text_ctxt=i18n_contexts.default)
        layout.operator("object.visual_transform_apply", text="Visual Transform")
        # layout.operator("object.duplicates_make_real")


class VIEW3D_MT_rorigintransform(bpy.types.Menu):
    bl_context = "objectmode"
    bl_label = "Move Origin"

    def draw(self, context):
        
        layout = self.layout
        
        layout.operator_context = 'EXEC_AREA'
        #layout.operator("object.origin_set", text="Geometry to Origin").type = 'GEOMETRY_ORIGIN'
        layout.operator("object.origin_set", text="Move Origin to Geometry").type = 'ORIGIN_GEOMETRY'
        layout.operator("object.origin_set", text="Move Origin to 3D Cursor").type = 'ORIGIN_CURSOR'

class VIEW3D_MT_robjectdata(bpy.types.Menu):
    bl_context = "objectmode"
    bl_label = "Object Data"

    def draw(self, context):
        
        layout = self.layout
        
        layout.operator("object.proxy_make", text="Make Proxy")
        layout.menu("VIEW3D_MT_make_links", text="Make Links")
        layout.operator("object.make_dupli_face")
        layout.operator_menu_enum("object.make_local", "type", text="Make Local")
        layout.menu("VIEW3D_MT_make_single_user")
        layout.operator("object.duplicates_make_real")
        layout.operator_menu_enum("object.convert", "target")

            
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

    def projectCursor(self, event):

        coord = mathutils.Vector((event.mouse_region_x, event.mouse_region_y))

        transform = bpy_extras.view3d_utils.region_2d_to_location_3d

        region = bpy.context.region

        rv3d = bpy.context.space_data.region_3d

        #### cursor used for the depth location of the mouse

        depth_location = bpy.context.scene.cursor_location

        ### creating 3d vector from the cursor

        end = transform(region, rv3d, coord, depth_location)
        
        ### Viewport origin

        start = bpy_extras.view3d_utils.region_2d_to_origin_3d(region, rv3d, coord)
        
        ### Cast ray from view to mouselocation

        ray = bpy.context.scene.ray_cast(start, start+(end-start)*2000)
        
        return start, end, ray

    def execute(self, context):
        
        # rayStart,rayEnd, ray = self.projectCursor(event)

        # if ray[0] == True:

        #    bpy.context.scene.cursor_location = ray[3]
        
        return {'FINISHED'}

class rmove_to_layer(bpy.types.Operator):
    
    bl_idname = "object.rmove_to_layer"
    bl_label = "rMoveToLayer"
    bl_description = "rMoveToLayer"
    bl_register = True

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        bpy.ops.object.move_to_layer()
        
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
    







