from pyfbsdk import*

# キャラクタライズに使用されているボーンをグループ化
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


# キャラクタライズされたモデルのメッシュをグループ化
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


# キャラクタライズされたモデル内の全てのボーンの数を数える
def BoneNum(chara:FBCharacter) -> int:
    returnNum = 0
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            returnNum += 1
    return returnNum

# CharacterのReferenceに何かしら割り当てされているか確認
def isSetReference(chara:FBCharacter) -> bool:
    prop = chara.PropertyList.Find("ReferenceLink")
    if len(prop) > 0:
        return True
    else:
        return False


# キャラクタライズされたモデルのシェイプキーについて調べる
def ShapeKey(chara:FBCharacter, option):
    ShapeKeyList = list()
    meshList = FBModelList()
    chara.GetSkinModelList(meshList)
    count = 0
    for mesh in meshList:
        # 各メッシュについて、新しくシェイプキーを検出したらリストに加える
        geo = mesh.Geometry
        for i in range(geo.ShapeGetCount()):
            name = geo.ShapeGetName(i)
            if not name in ShapeKeyList:
                ShapeKeyList.append(name)
            # 既にリストに登録済みのシェイプキーを検出したらcountを増やす
            else:
                count += 1

    # 全てのシェイプキーの数を返す
    if option == "Num":
        return len(ShapeKeyList)
    
    # 複数メッシュにまたがるシェイプキーがあったのならTrueを返す
    if option == "InMultipleModel":
        if count > 1: 
            return True
        else:
            return False


if __name__ == "__main__":
    chara = FBApplication().CurrentCharacter
    if chara == None:
        FBMessageBox("Cauton", "Error : Select a Charater", "OK")
        del(chara)

    else:
        SkeletonGroup(chara, "g")
        MeshGroup(chara, "g")
        FBMessageBox("Result",
                        "Character Skeleton group / Mesh group Created." + "\n" + \
                        "Check them in Resources Window >> Groups","OK")

        BoneNumResult = BoneNum(chara)        
        ShapeNumResult = ShapeKey(chara,"Num")
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
        
        del(chara, BoneNumResult, ShapeNumResult, multiResult, refResult)