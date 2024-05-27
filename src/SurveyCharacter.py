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

        def ShapeKey(chara, option):
            ShapeKeyList = list()
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
                print(ShapeKeyList)
                return str(len(ShapeKeyList))
            
            if option == "InMultipleModel":
                if count > 1: 
                    return "Yes"
                else:
                    return "No"
                
        FBMessageBox("Result", 
                      "Bone number : " + BoneNum(chara) + "\n" \
                    + "ShapeKey number : " + ShapeKey(chara, "Num") + "\n" \
                    + "ShapeKey in Muletiple Model : " + ShapeKey(chara, "InMultipleModel") + "\n" \
                    + "Reference : " + isSetReference(chara), "OK")
        
except:
    FBMessageBox("Cauton", "Error : Select a Charater", "OK")