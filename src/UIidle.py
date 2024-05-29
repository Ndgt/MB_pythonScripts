
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
        print(FBApplication().ExecuteScript(r"C:\\Users\\owner\\vscode\\MB_pythonScripts\\src\\AddModuleButton.py"))
    
    else:
        print("EventOff")
        lSysOnUIIdle.Remove(RunStartUp)
 
lSysOnUIIdle.Add(RunStartUp)