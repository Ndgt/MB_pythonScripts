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

import UIfunctions


# Qtウィジェットを子とする親のMotionBuilderウィジェットを定義
class WidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.ParentedWidgetObject = UIfunctions.ParentedWidget(wrapInstance(pWigParent, QtWidgets.QWidget))
        return getCppPointer(self.ParentedWidgetObject)[0]


# 上記ウィジェットをUIとするPython Toolを定義
class WigTool(FBTool):
    def PopulateLayout(self):
        # Add Layout and set control in Qt widget Holder
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


# Tool名を定義
toolName = "ActorSetHelper"

# すでに同じ名前のToolが作成されていたらそれを削除
FBDestroyToolByName(toolName)

# 定義したToolをPython Tool Managerに追加
tool = WigTool(toolName)
FBAddTool(tool)

# Tool を表示
ShowTool(tool)