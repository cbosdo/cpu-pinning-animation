import os.path
import os
import bpy

folder = os.path.dirname(bpy.data.filepath)
output = os.path.join(folder, "output")

if not os.path.exists(output):
    os.mkdir(output)

bpy.ops.screen.frame_jump()
i = 0
while 'FINISHED' in bpy.ops.screen.keyframe_jump(next=True):
    # Render the scene as png
    picname = "%02d.png" % i
    bpy.context.scene.render.filepath = os.path.join(output, picname)
    print ("Rendering image %s" % picname)
    bpy.ops.render.render(animation=False, write_still=True)
    i = i + 1
