import pyfbsdk
from pyfbsdk import FBApplication, FBFindModelByLabelName, FBGroup, FBPropertyListObject

chara = FBApplication().CurrentCharacter

group = FBGroup("CharacterSkeleton")

for prop in chara.PropertyList:
    if type(prop) == pyfbsdk.FBPropertyListObject:
        if len(prop) > 0 and not "Solver" in prop.Name:
            for j in range(len(prop)):
                if type(prop[j]) == pyfbsdk.FBModelSkeleton:
                    group.ConnectSrc(prop[j])

del(chara, group, FBApplication, FBFindModelByLabelName, FBGroup, FBPropertyListObject)
