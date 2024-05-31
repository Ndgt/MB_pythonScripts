from pyfbsdk import FBMessageBox

'''
import your module here
'''

import charainfo

try:    
    from PySide6.QtCore import*
    from PySide6.QtWidgets import*

except:
    from PySide2.QtCore import*
    from PySide2.QtWidgets import*    

# get access of Viewer menu widget
def main():
    for win in QApplication.topLevelWidgets():  
        if win.accessibleName() == "Mainboard":
            for dwgt in win.findChildren(QDockWidget):
                if dwgt.windowTitle() == "Viewer":
                    GetMenuwgtInfo(dwgt)

# search and get information of display button in Viewer menu widget
def GetMenuwgtInfo(wgt:QDockWidget):
    lymng = wgt.layout()
    for i in range(lymng.count()):
        for childwgt in lymng.itemAt(i).widget().children():
            if childwgt.accessibleName() == "SingleTool":
                for childbarwgt in childwgt.children():
                    if childbarwgt.accessibleName() == "ButtonBarWithRightBar":
                        viewerMenuwgt = childbarwgt
                        for menu in viewerMenuwgt.findChildren(QWidget):
                            if menu.accessibleName() == "Display":
                                displayGeo = menu.geometry()
                                CreateMenu(viewerMenuwgt,displayGeo)
                                
# create original menu
def CreateMenu(viewerMenuwgt, displayGeo):
    # create a button and change the caption as you like
    button = QPushButton("charainfo",viewerMenuwgt)

    # set the size of button
    x = displayGeo.right() + 80
    y = displayGeo.top()
    w = 70
    h = displayGeo.bottom()-displayGeo.top()
    button.setGeometry(x,y,w,h)

    # set the style of the button
    button.setStyleSheet("color: black; background-color:#ADD8E6;")

    # connect your module methods to the button
    button.clicked.connect(charainfo.SurveyAll)

    # show button
    button.show()

main()