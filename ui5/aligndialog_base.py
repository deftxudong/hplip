# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui5/aligndialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(700, 568)
        self.gridlayout = QtWidgets.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label, 0, 0, 1, 3)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line, 1, 0, 1, 5)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridlayout.addWidget(self.line_2, 3, 0, 1, 5)
        self.StepText = QtWidgets.QLabel(Dialog)
        self.StepText.setObjectName("StepText")
        self.gridlayout.addWidget(self.StepText, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(191, 29, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem, 4, 1, 1, 1)
        self.NextButton = QtWidgets.QPushButton(Dialog)
        self.NextButton.setObjectName("NextButton")
        self.gridlayout.addWidget(self.NextButton, 4, 3, 1, 1)
        self.CancelButton = QtWidgets.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.gridlayout.addWidget(self.CancelButton, 4, 4, 1, 1)
        self.StackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.StackedWidget.setObjectName("StackedWidget")
        self.StartPage = QtWidgets.QWidget()
        self.StartPage.setObjectName("StartPage")
        self.gridlayout1 = QtWidgets.QGridLayout(self.StartPage)
        self.gridlayout1.setObjectName("gridlayout1")
        self.DeviceComboBox = DeviceUriComboBox(self.StartPage)
        self.DeviceComboBox.setObjectName("DeviceComboBox")
        self.gridlayout1.addWidget(self.DeviceComboBox, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.StartPage)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridlayout2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridlayout2.setObjectName("gridlayout2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout2.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridlayout1.addWidget(self.groupBox, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(564, 161, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem1, 2, 0, 1, 1)
        self.StackedWidget.addWidget(self.StartPage)
        self.LoadPaperPage = QtWidgets.QWidget()
        self.LoadPaperPage.setObjectName("LoadPaperPage")
        self.gridlayout3 = QtWidgets.QGridLayout(self.LoadPaperPage)
        self.gridlayout3.setObjectName("gridlayout3")
        self.LoadPaper = LoadPaperGroupBox(self.LoadPaperPage)
        self.LoadPaper.setTitle("")
        self.LoadPaper.setObjectName("LoadPaper")
        self.gridlayout3.addWidget(self.LoadPaper, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 181, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout3.addItem(spacerItem2, 1, 0, 1, 1)
        self.StackedWidget.addWidget(self.LoadPaperPage)
        self.PaperEdgePage = QtWidgets.QWidget()
        self.PaperEdgePage.setObjectName("PaperEdgePage")
        self.gridlayout4 = QtWidgets.QGridLayout(self.PaperEdgePage)
        self.gridlayout4.setObjectName("gridlayout4")
        self.PageEdgeTitle = QtWidgets.QLabel(self.PaperEdgePage)
        self.PageEdgeTitle.setText("")
        self.PageEdgeTitle.setObjectName("PageEdgeTitle")
        self.gridlayout4.addWidget(self.PageEdgeTitle, 0, 0, 1, 4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem4, 2, 0, 1, 1)
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.PageEdgeIcon = QtWidgets.QLabel(self.PaperEdgePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PageEdgeIcon.sizePolicy().hasHeightForWidth())
        self.PageEdgeIcon.setSizePolicy(sizePolicy)
        self.PageEdgeIcon.setMinimumSize(QtCore.QSize(85, 90))
        self.PageEdgeIcon.setMaximumSize(QtCore.QSize(85, 90))
        self.PageEdgeIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.PageEdgeIcon.setObjectName("PageEdgeIcon")
        self.hboxlayout.addWidget(self.PageEdgeIcon)
        self.PageEdgeComboBox = QtWidgets.QComboBox(self.PaperEdgePage)
        self.PageEdgeComboBox.setObjectName("PageEdgeComboBox")
        self.hboxlayout.addWidget(self.PageEdgeComboBox)
        self.gridlayout4.addLayout(self.hboxlayout, 2, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem5, 2, 3, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem6, 3, 2, 1, 1)
        self.StackedWidget.addWidget(self.PaperEdgePage)
        self.AlignmentNumber = QtWidgets.QWidget()
        self.AlignmentNumber.setObjectName("AlignmentNumber")
        self.gridlayout5 = QtWidgets.QGridLayout(self.AlignmentNumber)
        self.gridlayout5.setObjectName("gridlayout5")
        self.AlignmentNumberTitle = QtWidgets.QLabel(self.AlignmentNumber)
        self.AlignmentNumberTitle.setText("")
        self.AlignmentNumberTitle.setObjectName("AlignmentNumberTitle")
        self.gridlayout5.addWidget(self.AlignmentNumberTitle, 0, 0, 1, 4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem7, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem8, 2, 0, 1, 1)
        self.hboxlayout1 = QtWidgets.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.AlignmentNumberIcon = QtWidgets.QLabel(self.AlignmentNumber)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AlignmentNumberIcon.sizePolicy().hasHeightForWidth())
        self.AlignmentNumberIcon.setSizePolicy(sizePolicy)
        self.AlignmentNumberIcon.setMinimumSize(QtCore.QSize(85, 90))
        self.AlignmentNumberIcon.setMaximumSize(QtCore.QSize(85, 90))
        self.AlignmentNumberIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AlignmentNumberIcon.setObjectName("AlignmentNumberIcon")
        self.hboxlayout1.addWidget(self.AlignmentNumberIcon)
        self.AlignmentNumberComboBox = QtWidgets.QComboBox(self.AlignmentNumber)
        self.AlignmentNumberComboBox.setObjectName("AlignmentNumberComboBox")
        self.hboxlayout1.addWidget(self.AlignmentNumberComboBox)
        self.gridlayout5.addLayout(self.hboxlayout1, 2, 1, 1, 2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem9, 2, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem10, 3, 2, 1, 1)
        self.StackedWidget.addWidget(self.AlignmentNumber)
        self.ColorAdjPage = QtWidgets.QWidget()
        self.ColorAdjPage.setObjectName("ColorAdjPage")
        self.gridlayout6 = QtWidgets.QGridLayout(self.ColorAdjPage)
        self.gridlayout6.setObjectName("gridlayout6")
        self.label_12 = QtWidgets.QLabel(self.ColorAdjPage)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridlayout6.addWidget(self.label_12, 0, 0, 1, 5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout6.addItem(spacerItem11, 1, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout6.addItem(spacerItem12, 2, 0, 1, 1)
        self.ColorAdjustIcon = QtWidgets.QLabel(self.ColorAdjPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ColorAdjustIcon.sizePolicy().hasHeightForWidth())
        self.ColorAdjustIcon.setSizePolicy(sizePolicy)
        self.ColorAdjustIcon.setMinimumSize(QtCore.QSize(85, 90))
        self.ColorAdjustIcon.setMaximumSize(QtCore.QSize(85, 90))
        self.ColorAdjustIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.ColorAdjustIcon.setText("")
        self.ColorAdjustIcon.setObjectName("ColorAdjustIcon")
        self.gridlayout6.addWidget(self.ColorAdjustIcon, 2, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout6.addItem(spacerItem13, 2, 2, 1, 1)
        self.hboxlayout2 = QtWidgets.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")
        self.ColorAdjustLabel = QtWidgets.QLabel(self.ColorAdjPage)
        self.ColorAdjustLabel.setObjectName("ColorAdjustLabel")
        self.hboxlayout2.addWidget(self.ColorAdjustLabel)
        self.ColorAdjustComboBox = QtWidgets.QComboBox(self.ColorAdjPage)
        self.ColorAdjustComboBox.setObjectName("ColorAdjustComboBox")
        self.hboxlayout2.addWidget(self.ColorAdjustComboBox)
        self.gridlayout6.addLayout(self.hboxlayout2, 2, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout6.addItem(spacerItem14, 2, 4, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout6.addItem(spacerItem15, 3, 1, 1, 1)
        self.StackedWidget.addWidget(self.ColorAdjPage)
        self.LBowPage = QtWidgets.QWidget()
        self.LBowPage.setObjectName("LBowPage")
        self.gridlayout7 = QtWidgets.QGridLayout(self.LBowPage)
        self.gridlayout7.setObjectName("gridlayout7")
        self.LBowTitle = QtWidgets.QLabel(self.LBowPage)
        self.LBowTitle.setText("")
        self.LBowTitle.setWordWrap(True)
        self.LBowTitle.setObjectName("LBowTitle")
        self.gridlayout7.addWidget(self.LBowTitle, 0, 0, 1, 5)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout7.addItem(spacerItem16, 1, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(41, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem17, 2, 0, 1, 1)
        self.LBowIcon = QtWidgets.QLabel(self.LBowPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBowIcon.sizePolicy().hasHeightForWidth())
        self.LBowIcon.setSizePolicy(sizePolicy)
        self.LBowIcon.setMinimumSize(QtCore.QSize(192, 93))
        self.LBowIcon.setMaximumSize(QtCore.QSize(192, 93))
        self.LBowIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.LBowIcon.setText("")
        self.LBowIcon.setObjectName("LBowIcon")
        self.gridlayout7.addWidget(self.LBowIcon, 2, 1, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem18, 2, 2, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem19, 2, 4, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout7.addItem(spacerItem20, 3, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.LBowPage)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridlayout8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridlayout8.setObjectName("gridlayout8")
        self.hboxlayout3 = QtWidgets.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.hboxlayout3.addWidget(self.label_4)
        self.aComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.aComboBox.setObjectName("aComboBox")
        self.hboxlayout3.addWidget(self.aComboBox)
        self.gridlayout8.addLayout(self.hboxlayout3, 0, 0, 1, 1)
        self.hboxlayout4 = QtWidgets.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.hboxlayout4.addWidget(self.label_5)
        self.bComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.bComboBox.setObjectName("bComboBox")
        self.hboxlayout4.addWidget(self.bComboBox)
        self.gridlayout8.addLayout(self.hboxlayout4, 1, 0, 1, 1)
        self.hboxlayout5 = QtWidgets.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.hboxlayout5.addWidget(self.label_6)
        self.cComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.cComboBox.setObjectName("cComboBox")
        self.hboxlayout5.addWidget(self.cComboBox)
        self.gridlayout8.addLayout(self.hboxlayout5, 2, 0, 1, 1)
        self.hboxlayout6 = QtWidgets.QHBoxLayout()
        self.hboxlayout6.setObjectName("hboxlayout6")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.hboxlayout6.addWidget(self.label_7)
        self.dComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.dComboBox.setObjectName("dComboBox")
        self.hboxlayout6.addWidget(self.dComboBox)
        self.gridlayout8.addLayout(self.hboxlayout6, 3, 0, 1, 1)
        self.hboxlayout7 = QtWidgets.QHBoxLayout()
        self.hboxlayout7.setObjectName("hboxlayout7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.hboxlayout7.addWidget(self.label_8)
        self.eComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.eComboBox.setObjectName("eComboBox")
        self.hboxlayout7.addWidget(self.eComboBox)
        self.gridlayout8.addLayout(self.hboxlayout7, 4, 0, 1, 1)
        self.hboxlayout8 = QtWidgets.QHBoxLayout()
        self.hboxlayout8.setObjectName("hboxlayout8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.hboxlayout8.addWidget(self.label_9)
        self.fComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.fComboBox.setObjectName("fComboBox")
        self.hboxlayout8.addWidget(self.fComboBox)
        self.gridlayout8.addLayout(self.hboxlayout8, 5, 0, 1, 1)
        self.hboxlayout9 = QtWidgets.QHBoxLayout()
        self.hboxlayout9.setObjectName("hboxlayout9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.hboxlayout9.addWidget(self.label_10)
        self.gComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.gComboBox.setObjectName("gComboBox")
        self.hboxlayout9.addWidget(self.gComboBox)
        self.gridlayout8.addLayout(self.hboxlayout9, 6, 0, 1, 1)
        self.hboxlayout10 = QtWidgets.QHBoxLayout()
        self.hboxlayout10.setObjectName("hboxlayout10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.hboxlayout10.addWidget(self.label_11)
        self.hComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.hComboBox.setObjectName("hComboBox")
        self.hboxlayout10.addWidget(self.hComboBox)
        self.gridlayout8.addLayout(self.hboxlayout10, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.iComboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.iComboBox.setObjectName("iComboBox")
        self.horizontalLayout.addWidget(self.iComboBox)
        self.gridlayout8.addLayout(self.horizontalLayout, 8, 0, 1, 1)
        self.gridlayout7.addWidget(self.groupBox_2, 1, 3, 3, 1)
        self.StackedWidget.addWidget(self.LBowPage)
        self.AioPage = QtWidgets.QWidget()
        self.AioPage.setObjectName("AioPage")
        self.gridlayout9 = QtWidgets.QGridLayout(self.AioPage)
        self.gridlayout9.setObjectName("gridlayout9")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout9.addItem(spacerItem21, 0, 1, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout9.addItem(spacerItem22, 1, 0, 1, 1)
        self.AioIcon = QtWidgets.QLabel(self.AioPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AioIcon.sizePolicy().hasHeightForWidth())
        self.AioIcon.setSizePolicy(sizePolicy)
        self.AioIcon.setMinimumSize(QtCore.QSize(92, 120))
        self.AioIcon.setMaximumSize(QtCore.QSize(92, 120))
        self.AioIcon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.AioIcon.setText("")
        self.AioIcon.setObjectName("AioIcon")
        self.gridlayout9.addWidget(self.AioIcon, 1, 1, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridlayout9.addItem(spacerItem23, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.AioPage)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridlayout9.addWidget(self.label_3, 1, 3, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout9.addItem(spacerItem24, 2, 1, 1, 1)
        self.StackedWidget.addWidget(self.AioPage)
        self.FrontPanelPage = QtWidgets.QWidget()
        self.FrontPanelPage.setObjectName("FrontPanelPage")
        self.gridlayout10 = QtWidgets.QGridLayout(self.FrontPanelPage)
        self.gridlayout10.setObjectName("gridlayout10")
        self.label_13 = QtWidgets.QLabel(self.FrontPanelPage)
        self.label_13.setTextFormat(QtCore.Qt.RichText)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.gridlayout10.addWidget(self.label_13, 0, 0, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridlayout10.addItem(spacerItem25, 1, 0, 1, 1)
        self.StackedWidget.addWidget(self.FrontPanelPage)
        self.gridlayout.addWidget(self.StackedWidget, 2, 0, 1, 5)

        self.retranslateUi(Dialog)
        self.StackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HP Device Manager - Align Print Cartridges"))
        self.label.setText(_translate("Dialog", "Align Print Cartridges"))
        self.StepText.setText(_translate("Dialog", "Step %1 of %2"))
        self.NextButton.setText(_translate("Dialog", "Next >"))
        self.CancelButton.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the device to align and click <span style=\" font-style:italic;\">Next &gt;</span> to continue.</p></body></html>"))
        self.label_12.setText(_translate("Dialog", "Choose the numbered colored box that the color <b>best </b>matches the background color of the bar."))
        self.ColorAdjustLabel.setText(_translate("Dialog", "Line %1:"))
        self.label_4.setText(_translate("Dialog", "Row A:"))
        self.label_5.setText(_translate("Dialog", "Row B:"))
        self.label_6.setText(_translate("Dialog", "Row C:"))
        self.label_7.setText(_translate("Dialog", "Row D:"))
        self.label_8.setText(_translate("Dialog", "Row E:"))
        self.label_9.setText(_translate("Dialog", "Row F:"))
        self.label_10.setText(_translate("Dialog", "Row G:"))
        self.label_11.setText(_translate("Dialog", "Row H:"))
        self.label_14.setText(_translate("Dialog", "Row I:"))
        self.label_3.setText(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Follow these steps to complete the alignment:</span> </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1.</span> Place the alignment page, with the printed side facing down, on the scanner. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">2.</span> Press the <span style=\" font-style:italic;\">Enter</span> or <span style=\" font-style:italic;\">Scan</span> button on the printer. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3.</span> \"Alignment Complete\" will be displayed when the process is finished (on some models with a front panel display) or the green light that was blinking during the process will stop blinking and remain green (on some models without a front panel display).</p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Cartridge alignment on this printer is only available by accessing the front panel of the printer. </span>Please refer to the user guide for the printer for more information. Click <span style=\" font-style:italic;\">Finish</span> to exit.</p></body></html>"))

from .deviceuricombobox import DeviceUriComboBox
from .loadpapergroupbox import LoadPaperGroupBox
