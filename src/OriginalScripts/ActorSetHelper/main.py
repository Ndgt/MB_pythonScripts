from pyfbsdk import*
from pyfbsdk_additions import*

try:
    from PySide6 import QtWidgets
    from shiboken6 import wrapInstance, getCppPointer
except:
    from PySide2 import QtWidgets
    from shiboken2 import wrapInstance, getCppPointer    

import UIdiscription

# declare WidgetHolder class object
class WigHolder(FBWidgetHolder):
    def WidgetCreate(self, pWigParent):
        self.HoldedWidgetObject = UIdiscription.HoldedWidget(wrapInstance(pWigParent,
                                                             QtWidgets.QWidget))
        return getCppPointer(self.HoldedWidgetObject)[0]

# declare as FBTool 
class WigTool(FBTool):
    def PopulateLayout(self):
        x = FBAddRegionParam(0, FBAttachType.kFBAttachLeft,"")
        y = FBAddRegionParam(0, FBAttachType.kFBAttachTop,"")
        w = FBAddRegionParam(0, FBAttachType.kFBAttachRight,"")
        h = FBAddRegionParam(0, FBAttachType.kFBAttachBottom,"")
        self.AddRegion("mainLayout", "testWidget", x,y,w,h)
        self.SetControl("mainLayout", self.WigHolderObject)

    def __init__(self,name):
        super().__init__(name)
        self.WigHolderObject = WigHolder()
        self.PopulateLayout()
        self.StartSizeX = 300
        self.StartSizeY = 300

# set Tool name
toolName = "ActorSetHelper"

# delete the Tool if exists
FBDestroyToolByName(toolName)

tool = WigTool(toolName)
FBAddTool(tool)
ShowTool(tool)