#
# Pixel perfect UV mapping - Made by JoseluGames.
# Source: https://github.com/JoseluGames/BlenderScripts
# Version 0.0.1
# Under CC BY-NC-SA 4.0 https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode
#
# Modified by (If you modify this script add yourself to this list and please don't remove anyone):
#  - JoseluGames (twitter.com/JoseluGames)
#  - 
#

import bpy
import bmesh
import mathutils

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.uv.cube_project()

bpy.ops.object.mode_set(mode='OBJECT')

me = bpy.context.active_object.data
bm = bmesh.new()
bm.from_mesh(me)

uv_lay = bm.loops.layers.uv.active

print()
print("-----------------")
print()
print("STARTING MESH UVs POS CORRECTION")
print()
print("-----------------")
print()

face_index = 0

for face in bm.faces:
    print("-----------------")
    print("FACE " + str(face_index))
    print("-----------------")
    face_index += 1
    loop_index = 0
    lowest_index = 0
    
    for loop in face.loops:
        uv = loop[uv_lay].uv
        if uv.x < face.loops[lowest_index][uv_lay].uv.x:
            lowest_index = loop_index
        elif uv.y < face.loops[lowest_index][uv_lay].uv.y:
            lowest_index = loop_index
        loop_index += 1
    
    delta_from_origin = mathutils.Vector((0.0, 0.0)) - face.loops[lowest_index][uv_lay].uv

print()
print("-----------------")
print()
print("STARTING MESH UVs POS PIXELIZATION")
print()
print("-----------------")
print()

# Change this parameter to your texture size
textureSize = 128

for face in bm.faces:
    for loop in face.loops:
        uv = loop[uv_lay].uv
        uv *= (40 * 1) / textureSize

bm.to_mesh(me)
bm.free()

bpy.ops.object.mode_set(mode='OBJECT')

print()
print("-----------------")
print()
print("MESH UVs PIXEL CORRECTION FINISHED")
print()
print("-----------------")
print()