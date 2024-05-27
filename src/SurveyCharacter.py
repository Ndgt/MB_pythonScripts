# python API �̂����Apyfbsdk���W���[�����C���|�[�g
from pyfbsdk import*

try:
    # ���ݑI�𒆂�Character�iFBCharacter�^�j��ϐ�chara�ɑ��
    chara = FBApplication().CurrentCharacter

    # �ϐ�chara�Ɋm����FBCharacter�I�u�W�F�N�g��������ꂽ�̂Ȃ�ȉ���S�Ď��s
    if not chara == None:
        # �L�����N�^���C�Y�Ɏg�p����Ă���{�[�����O���[�v��
        def MakeCharacterSkeletonGroup(chara):
            groupname = chara.Name + "/Skeleton"
            group = FBGroup(groupname)
            for prop in chara.PropertyList:
                if prop.Name.endswith("Link") and len(prop) > 0:
                    group.ConnectSrc(prop[0])

        '''
        # ���̃R�[�h�ł����l�ɃO���[�v�����\
        def MakeCharacterSkeletonGroup2(chara):
            group = FBGroup("CharacterSkeleton")            
            BodyNodeIdList = list(vars(FBBodyNodeId)["values"].values())
            for id in BodyNodeIdList:
                model = chara.GetModel(id)
                if not model == None:
                    group.ConnectSrc(model)
        '''

        # ���b�V�����i�[���郊�X�g�iFBModelList�^�j��錾
        meshList = FBModelList()

        # �L�����N�^���C�Y���ꂽ���f���̃��b�V�����O���[�v��
        def MakeCharacterMeshGroup(chara):
            groupname = chara.Name + "/Mesh" 
            group = FBGroup(groupname)
            chara.GetSkinModelList(meshList)
            for mesh in meshList:
                group.ConnectSrc(mesh)

        # ��L�֐������s���A���ꂽ�O���[�v���m�F����悤�\��
        MakeCharacterSkeletonGroup(chara)
        MakeCharacterMeshGroup(chara)
        FBMessageBox("Result",
                     "Character Skeleton group / Mesh group Created." + "\n" + \
                     "Check them in Resources Window >> Groups","OK")

        # �L�����N�^���C�Y���ꂽ���f�����̑S�Ẵ{�[���̐��𐔂���
        def BoneNum(chara):
            returnNum = 0
            for prop in chara.PropertyList:
                if prop.Name.endswith("Link") and len(prop) > 0:
                    returnNum += 1
            return str(returnNum)

        # Character��Reference�ɉ������犄�蓖�Ă���Ă��邩�m�F
        def isSetReference(chara):
            prop = chara.PropertyList.Find("ReferenceLink")
            if len(prop) > 0:
                return "set"
            else:
                return "not set"

        # �L�����N�^���C�Y���ꂽ���f���̃V�F�C�v�L�[�ɂ��Ē��ׂ�
        def ShapeKey(chara, option):
            ShapeKeyList = list()
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
                print(ShapeKeyList)
                return str(len(ShapeKeyList))
            
            # �������b�V���ɂ܂�����V�F�C�v�L�[���������̂Ȃ�Yes��Ԃ�
            if option == "InMultipleModel":
                if count > 1: 
                    return "Yes"
                else:
                    return "No"
        
        # ���s���A���ʂ�\��
        FBMessageBox("Result", 
                      "Bone number : " + BoneNum(chara) + "\n" \
                    + "ShapeKey number : " + ShapeKey(chara, "Num") + "\n" \
                    + "ShapeKey in Muletiple Model : " + ShapeKey(chara, "InMultipleModel") + "\n" \
                    + "Reference : " + isSetReference(chara), "OK")
        
        # ���������
        del(chara, meshList)

# ���s����character���I������Ă��Ȃ�������G���[��\��
except:
    FBMessageBox("Cauton", "Error : Select a Charater", "OK")