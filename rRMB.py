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

    def clicked_on_view(self, context):

        print()

    def draw(self, context):
        
        obj = context.active_object
        mode_string = context.mode
        edit_object = context.edit_object
        layout = self.layout
        selected = context.selected_objects
        
        #Menus in All Modes
        
        layout.operator("view3d.cursor3d", text="Place 3d Cursor", icon="CURSOR")
        # layout.operator("view3d.rcursor3d", text="Place 3d Cursor", icon="CURSOR")
        layout.menu("VIEW3D_MT_rmovecursor")

        layout.separator()

        layout.operator_menu_enum("object.mode_set", "mode", text="Change Mode") 
        
        #Mode Specific Menus
        
        if edit_object:
            
            #Edit Mode
            
            if edit_object.type.lower() == "mesh":
                
                #Mesh

                layout.separator()

                layout.menu("VIEW3D_MT_edit_mesh_showhide")

                layout.menu("VIEW3D_MT_rselect_edit_mesh")

                layout.separator()

                obj.update_from_editmode()

                selected_verts = [v for v in obj.data.vertices if v.select]

                if len(selected_verts) > 0:

                    #--- Mesh With Vertices Selected

                    layout.menu("VIEW3D_MT_rcut")

                    layout.menu("VIEW3D_MT_rcreate")

                    layout.menu("VIEW3D_MT_rtransform")

                    layout.menu("VIEW3D_MT_rdeform")

                    layout.separator()
        
                    layout.menu("VIEW3D_MT_redit_mesh_vertices")
                    layout.menu("VIEW3D_MT_redit_mesh_edges")
                    layout.menu("VIEW3D_MT_redit_mesh_faces")

                    layout.menu("VIEW3D_MT_redit_mesh_normals")
                    
                    # layout.menu("VIEW3D_MT_edit_mesh_specials")

                    layout.separator()

                    layout.operator("mesh.duplicate_move", text = "Duplicate")

                    layout.operator_menu_enum("mesh.separate", "type", text = "Separate Into New Object")
                    
                    layout.menu("VIEW3D_MT_edit_mesh_delete")
                    
                    layout.separator()

                    layout.menu("VIEW3D_MT_rshape_keys_vertex_groups")

                    layout.menu("VIEW3D_MT_hook")

                    layout.separator()

                    layout.menu("VIEW3D_MT_edit_mesh_clean")
                    
                    layout.menu("VIEW3D_MT_uv_map", text="Unwrap")
                    
                    #layout.separator()
                    
                    #layout.operator("object.editmode_toggle", text="Exit Edit Mode")

                else:

                    #--- Mesh With Nothing Selected

                    layout.menu("VIEW3D_MT_rcut_nothing_selected")

                    layout.separator()

                    layout.label(text="Add:")
                    layout.operator("mesh.primitive_plane_add", text="Plane", icon='MESH_PLANE')
                    layout.operator("mesh.primitive_cube_add", text="Cube", icon='MESH_CUBE')
                    layout.operator("mesh.primitive_circle_add", text="Circle", icon='MESH_CIRCLE')
                    layout.operator("mesh.primitive_uv_sphere_add", text="UV Sphere", icon='MESH_UVSPHERE')
                    layout.operator("mesh.primitive_ico_sphere_add", text="Ico Sphere", icon='MESH_ICOSPHERE')
                    layout.operator("mesh.primitive_cylinder_add", text="Cylinder", icon='MESH_CYLINDER')
                    layout.operator("mesh.primitive_cone_add", text="Cone", icon='MESH_CONE')
                    layout.operator("mesh.primitive_torus_add", text="Torus", icon='MESH_TORUS')

                    layout.operator("mesh.primitive_grid_add", text="Grid", icon='MESH_GRID')
                    layout.operator("mesh.primitive_monkey_add", text="Monkey", icon='MESH_MONKEY')


                
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

                # layout.separator()

                # layout.prop_menu_enum(toolsettings, "proportional_edit")
                # layout.prop_menu_enum(toolsettings, "proportional_edit_falloff")

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

            #Object Mode
            
            #---Object Mode with Objects selected
            
            if len(selected)>0:

                # layout.separator()

                layout.menu("VIEW3D_MT_select_object")
                
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
                
                #---Object Mode without Objects selected
                
                layout.separator()
                
                layout.menu("VIEW3D_MT_object_showhide")
                layout.operator("view3d.pastebuffer", text="Paste")

                layout.separator()

                layout.operator_context = 'EXEC_REGION_WIN'

                #layout.operator_menu_enum("object.mesh_add", "type", text="Mesh", icon='OUTLINER_OB_MESH')
                layout.menu("INFO_MT_mesh_add", icon='OUTLINER_OB_MESH')

                #layout.operator_menu_enum("object.curve_add", "type", text="Curve", icon='OUTLINER_OB_CURVE')
                layout.menu("INFO_MT_curve_add", icon='OUTLINER_OB_CURVE')
                #layout.operator_menu_enum("object.surface_add", "type", text="Surface", icon='OUTLINER_OB_SURFACE')
                layout.menu("INFO_MT_surface_add", icon='OUTLINER_OB_SURFACE')
                layout.menu("INFO_MT_metaball_add", text="Metaball", icon='OUTLINER_OB_META')
                layout.operator("object.text_add", text="Text", icon='OUTLINER_OB_FONT')
                layout.separator()

                layout.menu("INFO_MT_armature_add", icon='OUTLINER_OB_ARMATURE')
                layout.operator("object.add", text="Lattice", icon='OUTLINER_OB_LATTICE').type = 'LATTICE'
                layout.operator_menu_enum("object.empty_add", "type", text="Empty", icon='OUTLINER_OB_EMPTY')
                layout.separator()

                layout.operator("object.speaker_add", text="Speaker", icon='OUTLINER_OB_SPEAKER')
                layout.separator()

                layout.operator("object.camera_add", text="Camera", icon='OUTLINER_OB_CAMERA')
                layout.operator_menu_enum("object.lamp_add", "type", text="Lamp", icon='OUTLINER_OB_LAMP')
                layout.separator()

                layout.operator_menu_enum("object.effector_add", "type", text="Force Field", icon='OUTLINER_OB_EMPTY')
                layout.separator()

                if len(bpy.data.groups) > 10:
                    layout.operator_context = 'INVOKE_REGION_WIN'
                    layout.operator("object.group_instance_add", text="Group Instance...", icon='OUTLINER_OB_EMPTY')
                else:
                    layout.operator_menu_enum("object.group_instance_add", "group", text="Group Instance", icon='OUTLINER_OB_EMPTY')
        
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
        
        
class VIEW3D_MT_rcut(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Cut"

    def draw(self, context):
        
        layout = self.layout

        layout.menu("VIEW3D_MT_rsubdivide")

        layout.separator()

        layout.operator("mesh.loopcut_slide")

        op = layout.operator("mesh.knife_tool", text="Knife All")
        op.use_occlude_geometry = True
        op.only_selected = False

        op = layout.operator("mesh.knife_tool", text="Knife Selected")
        op.use_occlude_geometry = False
        op.only_selected = True
        
        layout.separator()

        layout.operator("mesh.bisect", text="Plane Cut")

        layout.operator("mesh.knife_project", text="Cut With Object")

        layout.separator()

        layout.operator("mesh.rip_move")
        layout.operator("mesh.rip_move_fill")
        layout.operator("mesh.edge_split", text = "Rip Along Selected Edges")

        layout.separator()

        layout.operator("mesh.split", text = "Separate")

class VIEW3D_MT_rcut_nothing_selected(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Cut"

    def draw(self, context):
        
        layout = self.layout

        # layout.menu("VIEW3D_MT_rsubdivide")

        # layout.separator()

        layout.operator("mesh.loopcut_slide")

        # op = layout.operator("mesh.knife_tool", text="Knife All")
        # op.use_occlude_geometry = True
        # op.only_selected = False

        # op = layout.operator("mesh.knife_tool", text="Knife Selected")
        # op.use_occlude_geometry = False
        # op.only_selected = True
        
        # layout.separator()

        # layout.operator("mesh.bisect", text="Plane Cut")

        layout.operator("mesh.knife_project", text="Cut With Object")

        # layout.separator()

        # layout.operator("mesh.rip_move")
        # layout.operator("mesh.rip_move_fill")
        # layout.operator("mesh.split")


class VIEW3D_MT_rcreate(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Create"

    def draw(self, context):
        
        layout = self.layout

        layout.operator("mesh.edge_face_add")
        layout.operator("mesh.bridge_edge_loops", text="Bridge")

        layout.separator()

        layout.operator("view3d.edit_mesh_extrude_move_normal", text="Extrude")
        layout.operator("view3d.edit_mesh_extrude_move_shrink_fatten", text="Extrude Along Normals")
        layout.operator("view3d.edit_mesh_extrude_individual_move", text="Extrude Individual")

        layout.separator()

        layout.operator("mesh.fill", text = "Fill With Triangles")
        layout.operator("mesh.fill_grid")


class VIEW3D_MT_rdeform(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Deform"

    def draw(self, context):
        
        layout = self.layout

        layout.operator("transform.tosphere", text="To Sphere")
        layout.operator("transform.shear", text="Shear")
        layout.operator("transform.bend", text="Bend")
        layout.operator("transform.shrink_fatten", text="Shrink/Fatten")
        layout.operator("transform.push_pull", text="Push/Pull")
        layout.operator("object.vertex_warp", text="Warp")

        layout.separator()
        
        layout.operator("mesh.vertices_smooth", text = "Relax")
        layout.operator("object.vertex_random")
        layout.operator("mesh.noise", text = "Displace With Texture")


class VIEW3D_MT_rtransform(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Transform"

    def draw(self, context):
        
        layout = self.layout

        layout.operator("transform.translate", text="Grab/Move")
        layout.operator("transform.rotate", text="Rotate")
        layout.operator("transform.resize", text="Scale")
        # layout.operator("transform.shrink_fatten", text="Shrink/Fatten")

        layout.separator()

        layout.menu("VIEW3D_MT_mirror")

        layout.menu("VIEW3D_MT_rsymmetry")

        # layout.operator("transform.tosphere", text="To Sphere")
        # layout.operator("transform.shear", text="Shear")
        # layout.operator("transform.bend", text="Bend")
        # layout.operator("transform.push_pull", text="Push/Pull")
        # layout.operator("object.vertex_warp", text="Warp")
        # layout.operator("object.vertex_random", text="Randomize")


class VIEW3D_MT_rsubdivide(bpy.types.Menu):
    bl_context = "editmode"
    bl_label = "Subdivide"

    def draw(self, context):
        
        layout = self.layout

        layout.operator("mesh.subdivide", text="Simple").smoothness = 0.0
        layout.operator("mesh.subdivide", text="Smooth").smoothness = 1.0

        layout.separator()

        layout.operator("mesh.unsubdivide", text = "Unsubdivide")

class VIEW3D_MT_redit_mesh_vertices(bpy.types.Menu):
    bl_label = "Vertices"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("mesh.vert_connect", text="Connect")
        layout.operator("transform.vert_slide", text="Slide")
        # layout.operator("mesh.vertices_smooth", text = "Relax")

        layout.separator()

        layout.operator("mesh.merge")
        layout.operator("mesh.remove_doubles")
        # layout.operator("mesh.rip_move")
        # layout.operator("mesh.rip_move_fill")
        # layout.operator("mesh.split")
        # layout.operator_menu_enum("mesh.separate", "type")

        layout.separator()

        # op = layout.operator("mesh.mark_sharp", text="Shade Smooth")
        # op.use_verts = True
        # op.clear = True
        # layout.operator("mesh.mark_sharp", text="Shade Sharp").use_verts = True

        # layout.separator()

        layout.operator("mesh.bevel").vertex_only = True
        layout.operator("mesh.convex_hull")

        # layout.operator("mesh.blend_from_shape")

        # layout.operator("object.vertex_group_blend")
        # layout.operator("mesh.shape_propagate_to_all")

        # layout.separator()

        # layout.menu("VIEW3D_MT_vertex_group")
        # layout.menu("VIEW3D_MT_hook")

class VIEW3D_MT_redit_mesh_edges(bpy.types.Menu):
    bl_label = "Edges"

    def draw(self, context):
        layout = self.layout

        with_freestyle = bpy.app.build_options.freestyle
        scene = context.scene

        layout.operator_context = 'INVOKE_REGION_WIN'

        # layout.operator("mesh.edge_face_add")
        # layout.operator("mesh.subdivide")
        # layout.operator("mesh.unsubdivide")

        # layout.separator()

        # layout.operator("mesh.loop_multi_select", text="Edge Loop").ring = False
        # layout.operator("mesh.loop_multi_select", text="Edge Ring").ring = True
        layout.operator("transform.edge_slide")

        layout.separator()

        layout.operator("transform.edge_crease")

        layout.separator()

        layout.operator("mesh.bevel").vertex_only = False
        layout.operator("transform.edge_bevelweight")


        layout.separator()

        layout.operator("mesh.mark_seam").clear = False
        layout.operator("mesh.mark_seam", text="Clear Seam").clear = True

        layout.separator()

        layout.operator("mesh.mark_sharp")
        layout.operator("mesh.mark_sharp", text="Clear Sharp").clear = True

        layout.separator()

        if with_freestyle and not scene.render.use_shading_nodes:
            layout.operator("mesh.mark_freestyle_edge").clear = False
            layout.operator("mesh.mark_freestyle_edge", text="Clear Freestyle Edge").clear = True
            layout.separator()

        layout.operator("mesh.edge_rotate", text="Rotate Edge CW").use_ccw = False
        layout.operator("mesh.edge_rotate", text="Rotate Edge CCW").use_ccw = True

        # layout.separator()

        # layout.operator("mesh.edge_split")
        # layout.operator("mesh.bridge_edge_loops")

        # layout.separator()

        # layout.operator("mesh.loop_to_region")
        # layout.operator("mesh.region_to_loop")


class VIEW3D_MT_redit_mesh_faces(bpy.types.Menu):
    bl_label = "Faces"

    def draw(self, context):
        layout = self.layout

        with_freestyle = bpy.app.build_options.freestyle
        scene = context.scene

        layout.operator_context = 'INVOKE_REGION_WIN'

        # layout.operator("mesh.flip_normals")
        # layout.operator("mesh.edge_face_add")
        # layout.operator("mesh.fill")
        # layout.operator("mesh.fill_grid")
        layout.operator("mesh.inset")
        # layout.operator("mesh.bevel").vertex_only = False
        layout.operator("mesh.solidify")
        layout.operator("mesh.wireframe")

        layout.separator()

        if with_freestyle and not scene.render.use_shading_nodes:
            layout.operator("mesh.mark_freestyle_face").clear = False
            layout.operator("mesh.mark_freestyle_face", text="Clear Freestyle Face").clear = True
            layout.separator()

        layout.operator("mesh.poke")
        layout.operator("mesh.quads_convert_to_tris")
        layout.operator("mesh.tris_convert_to_quads")
        layout.operator("mesh.beautify_fill", text = "Rearrange Triangles (Beautify)")

        # layout.separator()

        # layout.operator("mesh.faces_shade_smooth")
        # layout.operator("mesh.faces_shade_flat")

        # layout.separator()

        # layout.operator("mesh.edge_rotate", text="Rotate Edge CW").use_ccw = False

        layout.separator()

        # layout.operator("mesh.uvs_rotate")
        # layout.operator("mesh.uvs_reverse")
        # layout.operator("mesh.colors_rotate")
        # layout.operator("mesh.colors_reverse")
        layout.menu("VIEW3D_MT_redit_mesh_faces_misc")


class VIEW3D_MT_redit_mesh_faces_misc(bpy.types.Menu):
    bl_label = "Miscellaneous"

    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.uvs_rotate")
        layout.operator("mesh.uvs_reverse")
        layout.operator("mesh.colors_rotate")
        layout.operator("mesh.colors_reverse")


class VIEW3D_MT_rshape_keys_vertex_groups(bpy.types.Menu):
    bl_label = "Object Data"

    def draw(self, context):
        layout = self.layout
        layout.operator_context = 'INVOKE_REGION_WIN'

        layout.operator("object.vertex_group_blend", text = "Blur Weights")

        layout.separator()

        layout.operator("mesh.blend_from_shape", text = "Morph to Shape Key")
        layout.operator("mesh.shape_propagate_to_all", text = "Propagate Shape To Other Shape Keys")

        layout.separator()

        layout.menu("VIEW3D_MT_vertex_group")

        layout.separator()

        layout.operator_menu_enum("mesh.sort_elements", "type", text="Sort Elements...")

        layout.operator("transform.translate", text = "Move Texture Space").texture_space = True
        layout.operator("transform.resize", text = "Scale Texture Space").texture_space = True


class VIEW3D_MT_redit_mesh_normals(bpy.types.Menu):
    bl_label = "Normals/Shading"

    def draw(self, context):
        layout = self.layout

        # layout.label("Normals:")
        layout.operator("mesh.normals_make_consistent", text="Normals Recalculate Outside").inside = False
        layout.operator("mesh.normals_make_consistent", text="Normals Recalculate Inside").inside = True

        layout.operator("mesh.flip_normals")

        layout.separator()

        # layout.label("Shading:")

        layout.operator("mesh.faces_shade_smooth")
        layout.operator("mesh.faces_shade_flat")


class VIEW3D_MT_rsymmetry(bpy.types.Menu):
    bl_label = "Symmetry"

    def draw(self, context):
        layout = self.layout

        layout.operator("mesh.symmetrize")
        layout.operator("mesh.symmetry_snap")   


class VIEW3D_MT_rselect_edit_mesh(bpy.types.Menu):
    bl_label = "Select"

    def draw(self, context):
        layout = self.layout

        layout.operator("view3d.select_border")
        layout.operator("view3d.select_circle")

        layout.separator()

        # primitive
        layout.operator("mesh.select_all").action = 'TOGGLE'
        layout.operator("mesh.select_all", text="Invert Selection").action = 'INVERT'
        layout.operator("mesh.select_linked", text="Linked")
        layout.operator("mesh.shortest_path_select", text="Shortest Path")

        layout.separator()
        
        layout.operator("mesh.loop_multi_select", text="Edge Loop").ring = False
        layout.operator("mesh.loop_multi_select", text="Edge Ring").ring = True

        layout.operator("mesh.loop_to_region")
        layout.operator("mesh.region_to_loop")

        layout.separator()

        layout.operator("mesh.select_more", text="More")
        layout.operator("mesh.select_less", text="Less")
        
        layout.separator()

        layout.operator("mesh.select_mirror", text="Mirror")
        layout.operator("mesh.select_axis", text="Side of Active")
        
        layout.separator()

        # numeric
        layout.operator("mesh.select_random", text="Random")
        layout.operator("mesh.select_nth")

        layout.separator()

        # geometric
        layout.operator("mesh.edges_select_sharp", text="Sharp Edges")
        layout.operator("mesh.faces_select_linked_flat", text="Linked Flat Faces")

        layout.separator()

        # topology
        layout.operator("mesh.select_loose", text="Loose Geometry")
        if context.scene.tool_settings.mesh_select_mode[2] is False:
            layout.operator("mesh.select_non_manifold", text="Non Manifold")
        layout.operator("mesh.select_interior_faces", text="Interior Faces")
        layout.operator("mesh.select_face_by_sides")

        layout.separator()

        # other ...
        layout.operator_menu_enum("mesh.select_similar", "type", text="Similar")
        layout.operator("mesh.select_ungrouped", text="Ungrouped Verts")




        
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
        
        # TODO

        # rayStart,rayEnd, ray = self.projectCursor(event)

        # if ray[0] == True:

        #    bpy.context.scene.cursor_location = ray[3]

        
        # bpy.ops.view3d.cursor3d()
        
        return {'FINISHED'}

class rMoveToLayer(bpy.types.Operator):
    
    bl_idname = "object.rmove_to_layer"
    bl_label = "rMoveToLayer"
    bl_description = "rMoveToLayer"
    bl_register = True

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):

        # TODO

        # bpy.ops.object.move_to_layer()
        
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
        kmi = km.keymap_items.new('view3d.cursor3d', 'RIGHTMOUSE', 'PRESS', alt=True)
        addon_keymaps.append((km, kmi))

def unregister():
    
    bpy.utils.unregister_module(__name__)
    
    wm = bpy.context.window_manager
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
        
if __name__ == "__main__":
    register()