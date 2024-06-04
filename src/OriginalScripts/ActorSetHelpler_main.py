# -*- coding: utf-8 -*-

from pyfbsdk import*
from pyfbsdk_additions import*

try:
    # for MotionBuilder 2025
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance, getCppPointer
     
except:
    # for MotionBuilder -2024
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance, getCppPointer    

from ActorSetHelper_Source import UIfunctions

class WidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.ParentedWidgetObject = UIfunctions.ParentedWidget(wrapInstance(pWigParent, QtWidgets.QWidget))
        return getCppPointer(self.ParentedWidgetObject)[0]


class WigTool(FBTool):
    def PopulateLayout(self):
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,"")
        self.AddRegion("ParetedWidget", "ActorSetHelper", x,y,w,h)
        self.SetControl("ParentedWidget", self.WidgetHolderObject)

    def __init__(self,name):
        super().__init__(name)
        self.WidgetHolderObject = WidgetHolder()
        self.PopulateLayout()
        self.StartSizeX = 300
        self.StartSizeY = 300


toolName = "ActorSetHelper"

FBDestroyToolByName(toolName)

tool = WigTool(toolName)
FBAddTool(tool)

ShowTool(tool)