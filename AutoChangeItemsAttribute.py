# select the attribute, you will find it's name in script editor
# set attr_name 
# set val you want to use
# select all the items you want to change the attribute
# run the script


import maya.cmds as cmds

def change_attr(attr_name, val):
    
    object_list = cmds.ls(sl=1)
    if len(object_list)>0:
        for object in object_list:
            try:
                object_shape = cmds.listRelatives(object, shapes=1)[0]
                cmds.setAttr("{}.{}".format(object_shape, attr_name), val)
            except IndexError:
                print ('{}对象没有shape节点'.foramt(object))

attr_name = 'aiExposure'
val = 10
     
change_attr(attr_name, val)
