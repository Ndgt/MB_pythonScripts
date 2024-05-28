from pyfbsdk import*

# �L�����N�^���C�Y�Ɏg�p����Ă���{�[�����O���[�v��
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


# �L�����N�^���C�Y���ꂽ���f���̃��b�V�����O���[�v��
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


# �L�����N�^���C�Y���ꂽ���f�����̑S�Ẵ{�[���̐��𐔂���
def BoneNum(chara:FBCharacter) -> int:
    returnNum = 0
    for prop in chara.PropertyList:
        if prop.Name.endswith("Link") and len(prop) > 0:
            returnNum += 1
    return returnNum

# Character��Reference�ɉ������犄�蓖�Ă���Ă��邩�m�F
def isSetReference(chara:FBCharacter) -> bool:
    prop = chara.PropertyList.Find("ReferenceLink")
    if len(prop) > 0:
        return True
    else:
        return False


# �L�����N�^���C�Y���ꂽ���f���̃V�F�C�v�L�[�ɂ��Ē��ׂ�
def ShapeKey(chara:FBCharacter, option):
    ShapeKeyList = list()
    meshList = FBModelList()
    chara.GetSkinModelList(meshList)
    count = 0
    for mesh in meshList:
        # �e���b�V���ɂ��āA�V�����V�F�C�v�L�[�����o�����烊�X�g�ɉ�����
        geo = mesh.Geometry
        for i in range(geo.ShapeGetCount()):
            name = geo.ShapeGetName(i)
            if not name in ShapeKeyList:
                ShapeKeyList.append(name)
            # ���Ƀ��X�g�ɓo�^�ς݂̃V�F�C�v�L�[�����o������count�𑝂₷
            else:
                count += 1

    # �S�ẴV�F�C�v�L�[�̐���Ԃ�
    if option == "Num":
        return len(ShapeKeyList)
    
    # �������b�V���ɂ܂�����V�F�C�v�L�[���������̂Ȃ�True��Ԃ�
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