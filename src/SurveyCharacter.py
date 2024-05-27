# python API のうち、pyfbsdkモジュールをインポート
from pyfbsdk import*

try:
    # 現在選択中のCharacter（FBCharacter型）を変数charaに代入
    chara = FBApplication().CurrentCharacter

    # 変数charaに確かにFBCharacterオブジェクトが代入されたのなら以下を全て実行
    if not chara == None:
        # キャラクタライズに使用されているボーンをグループ化
        def MakeCharacterSkeletonGroup(chara):
            groupname = chara.Name + "/Skeleton"
            group = FBGroup(groupname)
            for prop in chara.PropertyList:
                if prop.Name.endswith("Link") and len(prop) > 0:
                    group.ConnectSrc(prop[0])

        '''
        # 下のコードでも同様にグループ化が可能
        def MakeCharacterSkeletonGroup2(chara):
            group = FBGroup("CharacterSkeleton")            
            BodyNodeIdList = list(vars(FBBodyNodeId)["values"].values())
            for id in BodyNodeIdList:
                model = chara.GetModel(id)
                if not model == None:
                    group.ConnectSrc(model)
        '''

        # メッシュを格納するリスト（FBModelList型）を宣言
        meshList = FBModelList()

        # キャラクタライズされたモデルのメッシュをグループ化
        def MakeCharacterMeshGroup(chara):
            groupname = chara.Name + "/Mesh" 
            group = FBGroup(groupname)
            chara.GetSkinModelList(meshList)
            for mesh in meshList:
                group.ConnectSrc(mesh)

        # 上記関数を実行し、作られたグループを確認するよう表示
        MakeCharacterSkeletonGroup(chara)
        MakeCharacterMeshGroup(chara)
        FBMessageBox("Result",
                     "Character Skeleton group / Mesh group Created." + "\n" + \
                     "Check them in Resources Window >> Groups","OK")

        # キャラクタライズされたモデル内の全てのボーンの数を数える
        def BoneNum(chara):
            returnNum = 0
            for prop in chara.PropertyList:
                if prop.Name.endswith("Link") and len(prop) > 0:
                    returnNum += 1
            return str(returnNum)

        # CharacterのReferenceに何かしら割り当てされているか確認
        def isSetReference(chara):
            prop = chara.PropertyList.Find("ReferenceLink")
            if len(prop) > 0:
                return "set"
            else:
                return "not set"

        # キャラクタライズされたモデルのシェイプキーについて調べる
        def ShapeKey(chara, option):
            ShapeKeyList = list()
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
                print(ShapeKeyList)
                return str(len(ShapeKeyList))
            
            # 複数メッシュにまたがるシェイプキーがあったのならYesを返す
            if option == "InMultipleModel":
                if count > 1: 
                    return "Yes"
                else:
                    return "No"
        
        # 実行し、結果を表示
        FBMessageBox("Result", 
                      "Bone number : " + BoneNum(chara) + "\n" \
                    + "ShapeKey number : " + ShapeKey(chara, "Num") + "\n" \
                    + "ShapeKey in Muletiple Model : " + ShapeKey(chara, "InMultipleModel") + "\n" \
                    + "Reference : " + isSetReference(chara), "OK")
        
        # メモリ解放
        del(chara, meshList)

# 実行時にcharacterが選択されていなかったらエラーを表示
except:
    FBMessageBox("Cauton", "Error : Select a Charater", "OK")