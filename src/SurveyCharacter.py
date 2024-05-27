from pyfbsdk import*

try:
    chara = FBApplication().CurrentCharacter

    if not chara == None:
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

        def MakeCharacterMeshGroup(chara):
            group = FBGroup("CharacterMesh")
            meshList = FBModelList()
            chara.GetSkinModelList(meshList)
            for mesh in meshList:
                group.ConnectSrc(mesh)

        FBMessageBox("Result", 
                    "Bone number : " + BoneNum(chara) + "\n" \
                    "Reference : " + isSetReference(chara),
                    "OK")

        MakeCharacterSkeletonGroup(chara)
        MakeCharacterMeshGroup(chara)
        FBMessageBox("Result","Character Skeleton group / Mesh group Created.\n \
                     Check them in Resources Window >> Groups","OK")

except:
    FBMessageBox("Cauton", "Error : Select a Charater", "OK")