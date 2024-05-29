from pyfbsdk import*

def SkeletonGroup(chara:FBCharacter, option = None):
    slist = FBModelList()
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            slist.append(prop[0])
    if option == None:
        return slist 
    if option == "g":
        groupname = chara.Name + "/Skeleton"
        group = FBGroup(groupname)
        for model in slist:
            group.ConnectSrc(model)

def MeshGroup(chara:FBCharacter, option = None):
    meshList = FBModelList()
    chara.GetSkinModelList(meshList) 
    if option == None:
        return meshList
    if option == "g":
        groupname = chara.Name + "/Mesh" 
        group = FBGroup(groupname)
        for mesh in meshList:
            group.ConnectSrc(mesh)

def BoneNum(chara:FBCharacter) -> int:
    returnNum = 0
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            returnNum += 1
    return returnNum

def isSetReference(chara:FBCharacter) -> bool:
    prop = chara.PropertyList.Find("ReferenceLink")
    if len(prop) > 0:
        return True
    else:
        return False

def ShapeKey(chara:FBCharacter, option):
    ShapeKeyList = list()
    meshList = FBModelList()
    chara.GetSkinModelList(meshList)
    count = 0
    for mesh in meshList:
        geo = mesh.Geometry
        for i in range(geo.ShapeGetCount()):
            name = geo.ShapeGetName(i)
            if not name in ShapeKeyList:
                ShapeKeyList.append(name)
            else:
                count += 1

    if option == "Num":
        return len(ShapeKeyList)
    
    if option == "InMultipleModel":
        if count > 1: 
            return True
        else:
            return False
        

########################
# if called by UI button
########################
def SurveyAll():
    chara = FBApplication().CurrentCharacter
    SkeletonGroup(chara, "g")
    MeshGroup(chara, "g")
    FBMessageBox("Result",
                    "Character Skeleton group / Mesh group Created." + "\n" + \
                    "Check them in Resources Window >> Groups","OK")

    BoneNumResult = str(BoneNum(chara))
    ShapeNumResult = str(ShapeKey(chara,"Num"))
    multiResult = "No"
    if ShapeKey(chara, "InMultipleModel"): multiResult = "Yes"
    refResult = "No"
    if isSetReference(chara): refResult = "Yes"

    FBMessageBox("Result", 
                "Bone number : " + BoneNumResult + "\n" \
                + "ShapeKey number : " + ShapeNumResult + "\n" \
                + "ShapeKey in Muletiple Model : " + multiResult + "\n" \
                + "Reference : " + refResult,
                "OK")
    del(chara,BoneNumResult,ShapeNumResult,refResult)


if __name__ in ("__main__", "builtins"):
    chara = FBApplication().CurrentCharacter
    if chara is None:
        FBMessageBox("Cauton", "Error : Select a Charater", "OK")
        del(chara)
    else:
        try:
            SkeletonGroup(chara, "g")
            MeshGroup(chara, "g")
            FBMessageBox("Result",
                            "Character Skeleton group / Mesh group Created." + "\n" + \
                            "Check them in Resources Window >> Groups","OK")

            BoneNumResult = str(BoneNum(chara))
            ShapeNumResult = str(ShapeKey(chara,"Num"))
            multiResult = "No"
            if ShapeKey(chara, "InMultipleModel"): multiResult = "Yes"
            refResult = "No"
            if isSetReference(chara): refResult = "Yes"

            FBMessageBox("Result", 
                        "Bone number : " + BoneNumResult + "\n" \
                        + "ShapeKey number : " + ShapeNumResult + "\n" \
                        + "ShapeKey in Muletiple Model : " + multiResult + "\n" \
                        + "Reference : " + refResult,
                        "OK")
        
        except Exception as err:
            FBMessageBox("caution", "An Error Occurred : {}".format(err), "OK") 

        finally:
            del(chara, BoneNumResult, ShapeNumResult, multiResult, refResult)