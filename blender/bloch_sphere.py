import bpy
bpy.ops.mesh.primitive_ico_sphere_add(location=(0, 0, 0))
obj = bpy.context.object

modifier = obj.modifiers.new('Subsurf', 'SUBSURF')
modifier.levels = 2
modifier.render_levels = 2

mesh = obj.data
for p in mesh.polygons:
    p.use_smooth = True