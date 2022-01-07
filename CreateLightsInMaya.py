
# Auto Generate Lights by reading txt

# txt:
# index:1;(1.0,3.0,5.0,1.0)
# index:2;(2.0,4.0,6.0,8.0)
# ...

# which means: light number;(x, y, z, intensity)



import maya.cmds as cmds
import sys

with open('d:\******\******.txt', 'r') as f:
    for line in f:
        index, info = line.split(';')

        num = index.split(':')[1]
        
        info = info[1:-2]
        x,y,z,intensity = info.split(',')
        x = float(x)
        y = float(y)
        z = float(z)
        intensity = float(intensity)
        # convert m to cm
        x *= 100
        y *= 100
        z *= 100
        
        object=cmds.pointLight(n=num, pos=[x,y,z], i=intensity)
#         set Arnold Exposure to 5
        cmds.setAttr("{}.{}".format(object, 'aiExposure'), 5)

        
