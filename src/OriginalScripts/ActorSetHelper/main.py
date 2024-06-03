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

import UIdescription


# define MotionBuilder class to hold child Qt Widget
class WidgetHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.ParentedWidgetObject = UIdescription.ParentedWidget(wrapInstance(pWigParent, QtWidgets.QWidget))
        return getCppPointer(self.ParentedWidgetObject)[0]


# define FBTool class
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


# set theTool name
toolName = "ActorSetHelper"

# delete the Tool if exists
FBDestroyToolByName(toolName)

# Add the Tool into Python Tool Manager
tool = WigTool(toolName)
FBAddTool(tool)

ShowTool(tool)