# -*- coding: utf-8 -*-

from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except: 
    from PySide2 import QtWidgets


from ui_mainwidget import Ui_toolWidget
import BodyIndex


class ParentedWidget(QtWidgets.QWidget, Ui_toolWidget()):
    def __init__(self, pWidgetHolder):
        super().__init__(pWidgetHolder)
        self.setupUi(self)
        # particular number in FBSkeletonNodeId class enum
        self.ActorPartsIndex = [21, 11, 16, 12, 1, 15, 14, 19, 18, 4, 3, 8, 7, 2, 5, 6, 9, 10, 13, 17, 20]
        self.TrackerIndex = [21, 11, 16, 12, 1, 15, 14, 19, 18, 4, 3, 8, 7]


    # function to Create new Actor and MarkerSet
    def CreateActor_MarkerSet(self):
        # lists to hold default settings of Actor
        self.defaultPivotPositionList = list()
        self.defaultOffsetList = list()
        self.defaultVectorList = list()
        self.pivotPropertyList = list()
        self.offsetPropertyList = list()

        # ActorとMarkerSetを作成
        self.actor = FBActor("HubActor")
        self.actor.MarkerSet = FBMarkerSet("MarkersetToHubActor")
        
        # extract enum in FBSkeletonNodeId class 
        self.SNodeIdList = list(vars(FBSkeletonNodeId)["values"].values())
        # set lists to hold default positions(pivot positions) and offsets of each parts in Actor

        for prop in self.actor.PropertyList:
            if not prop.Name.find("Position") == -1:
                # FBPropertyAnimatableVector3d.Data returns FBVector3d class object
                self.defaultPivotPositionList.append(prop.Data)
                self.pivotPropertyList.append(prop)
            if not prop.Name.find("Offset") == -1 and not prop.Name == "ManipulateOffsets":
                self.defaultOffsetList.append(prop.Data)
                self.offsetPropertyList.append(prop)

        self.vlist = FBVector3d()
        self.hipsvector = FBVector3d()
        self.actor.GetDefinitionTranslationVector(self.SNodeIdList[1],self.hipsvector)

        for i in self.ActorPartsIndex:
            self.actor.GetDefinitionTranslationVector(self.SNodeIdList[i],self.vlist)
            self.defaultVectorList.append(self.vlist-self.hipsvector)


    # 選択した一つのオブジェクトの位置にActorの腰を移動させる
    def FitToTrackers(self):
        targetmodel = FBModelList()
        targetposition = FBVector3d()
        FBGetSelectedModels(targetmodel)
        
        targetmodel[0].GetVector(targetposition, FBModelTransformationType.kModelTransformation)
        self.actor.SetActorTranslation(targetposition)


    # y軸中心にActorを180°回転させる
    def RotateYdeg(self):
        rlist = FBVector3d()

        # Actorの現時点の回転座標を得る
        self.actor.GetDefinitionRotationVector(BodyIndex.AllActorIndex.values[0],rlist) 
        
        # 180°分の回転を加える
        self.actor.SetDefinitionRotationVector(BodyIndex.AllActorIndex.values[0],rlist + FBVector3d(0,180,0))


    # function to force Actor to T-Pose
    def MakeActorDefaultTPose(self):
        # get hips position and reset hips rotation
        self.hipsvectornew = FBVector3d()
        self.actor.SetDefinitionRotationVector(self.SNodeIdList[1], FBVector3d(0,0,0))
        self.actor.GetDefinitionTranslationVector(self.SNodeIdList[1], self.hipsvectornew)

        for i in range(len(self.pivotPropertyList)):
            # reset pivot position
            self.pivotPropertyList[i].Data = self.defaultPivotPositionList[i]
        for i in range(len(self.offsetPropertyList)):
            # reset offset
            self.offsetPropertyList[i].Data = self.defaultOffsetList[i]

        vectorcount = 0
        for i in self.ActorPartsIndex:
            if not i == 1:
                # reset rotaton
                self.actor.SetDefinitionRotationVector(self.SNodeIdList[i],FBVector3d(0,0,0))
                # reset body parts position
                self.actor.SetDefinitionTranslationVector(self.SNodeIdList[i], self.hipsvectornew + self.defaultVectorList[vectorcount])
            vectorcount += 1
                

    # 直近に作成したActorとMarkerSetを削除し、Qt Sliderの位置を中心に戻す
    def ResetAll(self):
        self.msys = FBSystem()
        if len(self.msys.Scene.Actors) > 0 and len(self.msys.Scene.MarkerSets) > 0:  
            self.check = FBMessageBox("Caution", "the Actor and MarkerSet will be removed.\n Are you sure you want to continue?", "Yes","No")
            if self.check == 1:
                self.msys.Scene.Actors[-1].FBDelete()
                self.msys.Scene.MarkerSets[-1].FBDelete()
                # reset Qt horizontalSlider Position
                self.horizontalSlider.setSliderPosition(50)


    # Qt Sliderが動いた際にint値（初期値50、1~99で変化）を受け取り、アクターのサイズを変更
    def AdjustActorSize(self,int):
        for index in BodyIndex.AllActorIndex.values:
            self.actor.SetDefinitionScaleVector(index,FBVector3d(int/50,int/50,int/50)) 


    # MarkerSetにトラッカーを登録する
    def BindMarkerModel(self):
        for tracker in list(BodyIndex.MarkerSetIndex.keys()):
            model = FBFindModelByLabelName(tracker)
            for m in model.Children[0:4]:
                self.actor.MarkerSet.AddMarker(BodyIndex.MarkerSetIndex[tracker],m)
 
        FBMessageBox("message","Adding Marker was completed !\n See the Actor Settings","OK")


    # Snapを実行
    def SnapActor(self):
        self.actor.Snap(FBRecalcMarkerSetOffset.kFBRecalcMarkerSetOffsetTR)