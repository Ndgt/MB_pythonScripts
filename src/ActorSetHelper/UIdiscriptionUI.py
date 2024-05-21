# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWidgetUI.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

try:
    from PySide6 import QtCore
    from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
        QSizePolicy, QSlider, QVBoxLayout, QWidget)

except:
    from PySide2 import QtCore
    from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
        QMetaObject, QObject, QPoint, QRect,
        QSize, QTime, QUrl, Qt)
    from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
        QFont, QFontDatabase, QGradient, QIcon,
        QImage, QKeySequence, QLinearGradient, QPainter,
        QPalette, QPixmap, QRadialGradient, QTransform)
    from PySide2.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
        QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_testWidget(object):
    def setupUi(self, testWidget):
        if not testWidget.objectName():
            testWidget.setObjectName(u"testWidget")
        testWidget.resize(328, 301)
        self.verticalLayout_2 = QVBoxLayout(testWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CreateButton = QPushButton(testWidget)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateButton.sizePolicy().hasHeightForWidth())
        self.CreateButton.setSizePolicy(sizePolicy)
        self.CreateButton.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(10)
        self.CreateButton.setFont(font)

        self.verticalLayout.addWidget(self.CreateButton)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fitActorButton = QPushButton(testWidget)
        self.fitActorButton.setObjectName(u"fitActorButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fitActorButton.sizePolicy().hasHeightForWidth())
        self.fitActorButton.setSizePolicy(sizePolicy1)
        self.fitActorButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.fitActorButton)

        self.RotateButton = QPushButton(testWidget)
        self.RotateButton.setObjectName(u"RotateButton")
        sizePolicy1.setHeightForWidth(self.RotateButton.sizePolicy().hasHeightForWidth())
        self.RotateButton.setSizePolicy(sizePolicy1)
        self.RotateButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout.addWidget(self.RotateButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.DefaultTPoseButton = QPushButton(testWidget)
        self.DefaultTPoseButton.setObjectName(u"DefaultTPoseButton")
        sizePolicy1.setHeightForWidth(self.DefaultTPoseButton.sizePolicy().hasHeightForWidth())
        self.DefaultTPoseButton.setSizePolicy(sizePolicy1)
        self.DefaultTPoseButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.DefaultTPoseButton)

        self.ResetAllButton = QPushButton(testWidget)
        self.ResetAllButton.setObjectName(u"ResetAllButton")
        sizePolicy1.setHeightForWidth(self.ResetAllButton.sizePolicy().hasHeightForWidth())
        self.ResetAllButton.setSizePolicy(sizePolicy1)
        self.ResetAllButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_3.addWidget(self.ResetAllButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label = QLabel(testWidget)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalSlider = QSlider(testWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy2.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy2)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setSliderPosition(50)
        self.horizontalSlider.setTracking(False)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bindButton = QPushButton(testWidget)
        self.bindButton.setObjectName(u"bindButton")
        sizePolicy1.setHeightForWidth(self.bindButton.sizePolicy().hasHeightForWidth())
        self.bindButton.setSizePolicy(sizePolicy1)
        self.bindButton.setMinimumSize(QSize(0, 0))
        self.bindButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.bindButton)

        self.snapButton = QPushButton(testWidget)
        self.snapButton.setObjectName(u"snapButton")
        sizePolicy.setHeightForWidth(self.snapButton.sizePolicy().hasHeightForWidth())
        self.snapButton.setSizePolicy(sizePolicy)
        self.snapButton.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.snapButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(testWidget)

        self.CreateButton.connect(QtCore.SIGNAL("clicked()"), testWidget.CreateActor_MarkerSet)
        self.fitActorButton.connect(QtCore.SIGNAL("clicked()"), testWidget.FitToTrackers)
        self.RotateButton.connect(QtCore.SIGNAL("clicked()"), testWidget.RotateYdeg)
        self.DefaultTPoseButton.connect(QtCore.SIGNAL("clicked()"), testWidget.MakeActorDefaultTPose)
        self.ResetAllButton.connect(QtCore.SIGNAL("clicked()"), testWidget.ResetAll)
        self.horizontalSlider.connect(QtCore.SIGNAL("sliderMoved(int)"), testWidget.AdjustActorSize)
        self.bindButton.connect(QtCore.SIGNAL("clicked()"), testWidget.BindMarkerModel)
        self.snapButton.connect(QtCore.SIGNAL("clicked()"), testWidget.SnapActor)

        QMetaObject.connectSlotsByName(testWidget)
    # setupUi

    def retranslateUi(self, testWidget):
        testWidget.setWindowTitle(QCoreApplication.translate("testWidget", u"Form", None))
        self.CreateButton.setText(QCoreApplication.translate("testWidget", u"Create Actor, MarkerSet", None))
        self.fitActorButton.setText(QCoreApplication.translate("testWidget", u"Fit to Trackers", None))
        self.RotateButton.setText(QCoreApplication.translate("testWidget", u"Rotate y 180 degs.", None))
        self.DefaultTPoseButton.setText(QCoreApplication.translate("testWidget", u"Force Actor T-Pose", None))
        self.ResetAllButton.setText(QCoreApplication.translate("testWidget", u"Reset All", None))
        self.label.setText(QCoreApplication.translate("testWidget", u"<html><head/><body><p>Adjust Actor Size ( small &lt;--&gt; big )</p></body></html>", None))
        self.bindButton.setText(QCoreApplication.translate("testWidget", u"Bind MarkerModel", None))
        self.snapButton.setText(QCoreApplication.translate("testWidget", u"Snap", None))
    # retranslateUi

