from pyfbsdk import*

try:
    chara = FBApplication().CurrentCharacter

    SkeletonNodeIdList = list(vars(FBSkeletonNodeId)["values"].values())
    for id in SkeletonNodeIdList:
        model = chara.getModel(id)

    MeshList = list(vars(FBBodyNodeId)["values"].values())
    for id in MeshList:
        model = chara.GetModel(id)
        if not model == None:
            print(model.Name)

    def BoneNum(chara):
        returnNum = 0
        for prop in chara.PropertyList:
            if prop.Name.endswith("Link") and len(prop) > 0:
                returnNum += 1
        return str(returnNum)

    def isSetReference(chara):
        prop = chara.PropertyList.Find("ReferenceLink")
        if len(prop) > 0:
            return "set"
        else:
            return "not set"
        
    def MakeGroup(chara):
        group = FBGroup("CharacterSkeleton")
        for prop in chara.PropertyList:
            if prop.Name.endswith("Link") and len(prop) > 0:
                group.ConnectSrc(prop[0])
        if len(group.Items) > 0:
            return True


    FBMessageBox("Result", 
                "Bone number : " + BoneNum(chara) + "\n" \
                "Reference : " + isSetReference(chara),
                "OK")

    if MakeGroup(chara):
        FBMessageBox("Result","Character bone group Created.\n\nCheck it in Resources Window >> Groups","OK")



except:
    FBMessageBox("Cauton", "Error : Select a Charater", "OK")