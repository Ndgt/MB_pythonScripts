try:    
    import PySide6
    from PySide6.QtCore import*
    from PySide6.QtWidgets import*

except:
    import PySide2
    from PySide2.QtCore import*
    from PySide2.QtWidgets import*    


def wsort(arr):
    arr.sort(key=lambda x: x[0])

def main():
    result = []
    for w in QApplication.topLevelWidgets():
        if type(w) == PySide6.QtWidgets.QMenu:
            name = w.title()

        if type(w) == PySide6.QtWidgets.QMainWindow:
            name = w.accessibleName()

        if type(w) == PySide6.QtWidgets.QWidget:
            name = w.accessibleName() 
        rows = w.geometry().left()
        cols = name
        addlist = [rows,w]
        result.append(addlist)
    
    wsort(result)

    for i in result:
        print(i,type(i[1]))

main()