import PySide6
from PySide6.QtWidgets import*
from PySide6.QtCore import*

try:    
    from PySide6.QtCore import*
    from PySide6.QtWidgets import*

except:
    from PySide2.QtCore import*
    from PySide2.QtWidgets import*   


for wgt in QApplication.topLevelWidgets():
    if type(wgt) == PySide6.QtWidgets.QMenu:
        print(wgt.title().rjust(20),type(wgt))

    if type(wgt) == PySide6.QtWidgets.QLabel:
        print(wgt.text().rjust(20),type(wgt))
    
    if type(wgt) == PySide6.QtWidgets.QWidget or type(wgt) == PySide6.QtWidgets.QTabWidget:
        print(wgt.accessibleName().rjust(20),type(wgt))
    
    if type(wgt) == PySide6.QtWidgets.QPushButton:
        print(wgt.accessibleName().rjust(20),type(wgt))