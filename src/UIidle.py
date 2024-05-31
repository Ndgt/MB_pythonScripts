
from pyfbsdk import *
 
lSystem = FBSystem()
lSysOnUIIdle = lSystem.OnUIIdle
 
lSysOnUIIdle.RemoveAll()
 
StartUp=-1
def RunStartUp(pOjbect, pEventName):
    global StartUp
    if StartUp==-1:
        print("RunStartUp")
        StartUp=0
        print(FBApplication().ExecuteScript(r"Users module")) # addpath , AddModuleButton
    
    else:
        print("EventOff")
        lSysOnUIIdle.Remove(RunStartUp)
 
lSysOnUIIdle.Add(RunStartUp)