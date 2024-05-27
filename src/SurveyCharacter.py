from pyfbsdk import*

try:
    chara = FBApplication().CurrentCharacter

    if not chara == None:
        def MakeCharacterSkeletonGroup(chara):
            group = FBGroup("CharacterSkeleton")
            for prop in chara.PropertyList:
                if prop.Name.endswith("Link") and len(prop) > 0:
                    group.ConnectSrc(prop[0])

        '''
        # below code is also serve as making skeleton group
        def MakeCharacterSkeletonGroup2(chara):
            group = FBGroup("CharacterSkeleton")            
            BodyNodeIdList = list(vars(FBBodyNodeId)["values"].values())
            for id in BodyNodeIdList:
                model = chara.GetModel(id)
                if not model == None:
                    group.ConnectSrc(model)
        '''

        meshList = FBModelList()
        def MakeCharacterMeshGroup(chara):
            group = FBGroup("CharacterMesh")
            chara.GetSkinModelList(meshList)
            for mesh in meshList:
                group.ConnectSrc(mesh)

        MakeCharacterSkeletonGroup(chara)
        MakeCharacterMeshGroup(chara)
        FBMessageBox("Result",
                     "Character Skeleton group / Mesh group Created." + "\n" + \
                     "Check them in Resources Window >> Groups","OK")


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

        def ShapeKeyNum(chara):
            ShapeKeyList = list()
            ModelNum = 1
            for mesh in meshList:
                geo = mesh.Geometry
                for i in range(geo.ShapeGetCount()):
                    name = geo.ShapeGetName(i)
                    if not name in ShapeKeyList:
                        ShapeKeyList.append(name)
                        if not mesh == meshList[0]:
                            ModelNum += 1
            return [str(len(ShapeKeyList)), ModelNum]


        FBMessageBox("Result", 
                      "Bone number : " + BoneNum(chara) + "\n" \
                    + "ShapeKey number : " + ShapeKeyNum(chara)[0] + "\n" \
                    + "Model number contains shapekey : " + ShapeKeyNum(chara)[1] + "\n" \
                    + "Reference : " + isSetReference(chara), "OK")


except:
    FBMessageBox("Cauton", "Error : Select a Charater", "OK")