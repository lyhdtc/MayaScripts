# import maya.OpenMaya as om
import maya.cmds as cmds
import sys

with open('/mnt/d/001Graduate/lightpos.txt', 'r') as f:
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
        
        cmds.pointLight(n=num, pos=[x,y,z], i=intensity)

        