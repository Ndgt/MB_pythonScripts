from pyfbsdk import FBMessageBox

try:
    from PySide6.QtCore import*
    from PySide6.QtWidgets import*

except:
    from PySide2.QtCore import*
    from PySide2.QtWidgets import*    

for win in QApplication.topLevelWidgets():
    if win.accessibleName() == "Mainboard":
        break
for dwgt in win.findChildren(QDockWidget):
    if dwgt.windowTitle() == "Viewer":
        break

def getMenuwgtInfo(wgt:QDockWidget):
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
                                return viewerMenuwgt, displayGeo


def HelloWorld():
    FBMessageBox("Viewer Button", "Viewer Button has clicked!", "OK")


viewerMenuwgt, displayGeo = getMenuwgtInfo(dwgt)
color = ["FF0000","FFA500","FFFF00","008000","00FFFF","0000FF","800080"]
for i , code in enumerate(color, 1):
    button = QPushButton("Hello",viewerMenuwgt)
    w = 60
    x = displayGeo.right() + 80 + (w+5)*(i-1)
    y = displayGeo.top()
    h = displayGeo.bottom()-displayGeo.top()
    button.setGeometry(x,y,w,h)
    button.clicked.connect(HelloWorld)
    button.setStyleSheet("background-color:#{};".format(code))
    button.show()