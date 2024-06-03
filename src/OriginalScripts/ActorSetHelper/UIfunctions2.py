from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
except: 
    from PySide2 import QtWidgets

from ui_mainwidget import Ui_toolWidget

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


    # function to Put Actor nearby selecetd Model
    def FitToTrackers(self):
        self.target = FBModelList()
        self.targetposition = FBVector3d()
        FBGetSelectedModels(self.target)
        # target[0]:selected Model
        # FBModel.GetVector returns a vector from the model
        self.target[0].GetVector(self.targetposition, FBModelTransformationType.kModelTransformation)
        self.actor.SetActorTranslation(self.targetposition)


    # function to Rotate Actor by 180 degrees around Y-axis
    def RotateYdeg(self):
        rlist = FBVector3d()
        # SNodeIdList[1]: Hips Bone of Actor
        self.actor.GetDefinitionRotationVector(self.SNodeIdList[1],rlist) 
        # rotate Actor
        self.actor.SetDefinitionRotationVector(self.SNodeIdList[1],rlist + FBVector3d(0,180,0))       


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
                

    # function to Delete Created Actor and MarkerSet
    def ResetAll(self):
        self.msys = FBSystem()
        if len(self.msys.Scene.Actors) > 0 and len(self.msys.Scene.MarkerSets) > 0:  
            self.check = FBMessageBox("Caution", "the Actor and MarkerSet will be removed.\n Are you sure you want to continue?", "Yes","No")
            if self.check == 1:
                self.msys.Scene.Actors[-1].FBDelete()
                self.msys.Scene.MarkerSets[-1].FBDelete()
                # reset Qt horizontalSlider Position
                self.horizontalSlider.setSliderPosition(50)

    # function to change the Size of Actor 
    # int: returned by Qt horizontalSlider when slider Moved
    def AdjustActorSize(self, int):
        for i in self.ActorPartsIndex:
            self.actor.SetDefinitionScaleVector(self.SNodeIdList[i],FBVector3d(int/50,int/50,int/50))   


    # function to register Trackers as Marker
    def BindMarkerModel(self):
        self.MarkerModelList = FBModelList()
        FBGetSelectedModels(self.MarkerModelList, None, True, True)
        if not len(self.MarkerModelList) == 79:
            FBMessageBox("Caution", "Choose All Models under \"RecordTarget\"", "OK")
        else:
            self.SkeletonNodeIdList = list()
            for i in self.TrackerIndex:
                self.SkeletonNodeIdList.append(self.SNodeIdList[i])
            for i in range(13):
                for j in range(4):
                    self.actor.MarkerSet.AddMarker(self.SkeletonNodeIdList[i], self.MarkerModelList[(6 * i + 1) + (j + 1)])
            FBMessageBox("message","Adding Marker was completed !\n See the HubActor Settings","OK")


    # function to execute Snap 
    def SnapActor(self):
        self.actor.Snap(FBRecalcMarkerSetOffset.kFBRecalcMarkerSetOffsetTR)