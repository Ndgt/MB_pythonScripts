from pyfbsdk import FBMessageBox
import charainfo

try:    
    from PySide6.QtCore import*
    from PySide6.QtWidgets import*

except:
    from PySide2.QtCore import*
    from PySide2.QtWidgets import*    


def main():
    for win in QApplication.topLevelWidgets():
        if win.accessibleName() == "Mainboard":
            for dwgt in win.findChildren(QDockWidget):
                if dwgt.windowTitle() == "Viewer":
                    GetMenuwgtInfo(dwgt)


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
                                

def CreateMenu(viewerMenuwgt, displayGeo):
    button = QPushButton("charainfo",viewerMenuwgt)
    x = displayGeo.right() + 80
    y = displayGeo.top()
    w = 70
    h = displayGeo.bottom()-displayGeo.top()
    button.setGeometry(x,y,w,h)
    button.clicked.connect(charainfo.SurveyAll)
    button.setStyleSheet("color: black; background-color:#ADD8E6;")
    button.show()

main()