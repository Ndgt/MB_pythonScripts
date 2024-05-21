from pyfbsdk import FBApplication, FBGroup, FBMessageBox

chara = FBApplication().CurrentCharacter
group = FBGroup("CharacterSkeleton")

for prop in chara.PropertyList:
    if not prop.Name.find("Link") == -1:
        if len(prop) > 0:
            for j in range(len(prop)):
                group.ConnectSrc(prop[j])


if len(group.Items) > 0:
    FBMessageBox("Character Successfully Confirmed","Check group in Resources Window >> Groups","OK")

del(chara, group,FBApplication,FBGroup,FBMessageBox)