# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psf_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PotentialSlopeFailureDialogBase(object):
    def setupUi(self, PotentialSlopeFailureDialogBase):
        PotentialSlopeFailureDialogBase.setObjectName("PotentialSlopeFailureDialogBase")
        PotentialSlopeFailureDialogBase.resize(494, 209)
        self.gridLayout = QtWidgets.QGridLayout(PotentialSlopeFailureDialogBase)
        self.gridLayout.setObjectName("gridLayout")
        self.progressBar = QtWidgets.QProgressBar(PotentialSlopeFailureDialogBase)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 8, 0, 1, 8)
        self.label_5 = QtWidgets.QLabel(PotentialSlopeFailureDialogBase)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 6, 1, 2)
        self.pushButtonSave = QtWidgets.QPushButton(PotentialSlopeFailureDialogBase)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.gridLayout.addWidget(self.pushButtonSave, 7, 8, 1, 1)
        self.label_8 = QtWidgets.QLabel(PotentialSlopeFailureDialogBase)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(PotentialSlopeFailureDialogBase)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(PotentialSlopeFailureDialogBase)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 9, 8, 1, 1)
        self.checkBoxIntoCanvas = QtWidgets.QCheckBox(PotentialSlopeFailureDialogBase)
        self.checkBoxIntoCanvas.setEnabled(True)
        self.checkBoxIntoCanvas.setObjectName("checkBoxIntoCanvas")
        self.gridLayout.addWidget(self.checkBoxIntoCanvas, 9, 1, 1, 7)
        self.widgetSOIL = QtWidgets.QWidget(PotentialSlopeFailureDialogBase)
        self.widgetSOIL.setMinimumSize(QtCore.QSize(175, 30))
        self.widgetSOIL.setObjectName("widgetSOIL")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widgetSOIL)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addWidget(self.widgetSOIL, 2, 6, 1, 3)
        self.runButton = QtWidgets.QPushButton(PotentialSlopeFailureDialogBase)
        self.runButton.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 8, 8, 1, 1)
        self.pushButtonHelp = QtWidgets.QPushButton(PotentialSlopeFailureDialogBase)
        self.pushButtonHelp.setObjectName("pushButtonHelp")
        self.gridLayout.addWidget(self.pushButtonHelp, 9, 0, 1, 1)
        self.spinBoxAlt = QtWidgets.QSpinBox(PotentialSlopeFailureDialogBase)
        self.spinBoxAlt.setEnabled(True)
        self.spinBoxAlt.setMaximum(89)
        self.spinBoxAlt.setProperty("value", 10)
        self.spinBoxAlt.setObjectName("spinBoxAlt")
        self.gridLayout.addWidget(self.spinBoxAlt, 5, 8, 1, 1)
        self.spinBoxIter = QtWidgets.QSpinBox(PotentialSlopeFailureDialogBase)
        self.spinBoxIter.setEnabled(True)
        self.spinBoxIter.setMaximum(360)
        self.spinBoxIter.setProperty("value", 16)
        self.spinBoxIter.setObjectName("spinBoxIter")
        self.gridLayout.addWidget(self.spinBoxIter, 5, 3, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 3, 1, 1)
        self.textOutput = QtWidgets.QLineEdit(PotentialSlopeFailureDialogBase)
        self.textOutput.setObjectName("textOutput")
        self.gridLayout.addWidget(self.textOutput, 7, 2, 1, 6)
        self.widgetDEM = QtWidgets.QWidget(PotentialSlopeFailureDialogBase)
        self.widgetDEM.setMinimumSize(QtCore.QSize(175, 30))
        self.widgetDEM.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.widgetDEM.setObjectName("widgetDEM")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widgetDEM)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.widgetDEM, 1, 6, 1, 3)
        self.label_2 = QtWidgets.QLabel(PotentialSlopeFailureDialogBase)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 6)
        self.label = QtWidgets.QLabel(PotentialSlopeFailureDialogBase)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 6)

        self.retranslateUi(PotentialSlopeFailureDialogBase)
        self.pushButton.clicked.connect(PotentialSlopeFailureDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(PotentialSlopeFailureDialogBase)

    def retranslateUi(self, PotentialSlopeFailureDialogBase):
        _translate = QtCore.QCoreApplication.translate
        PotentialSlopeFailureDialogBase.setWindowTitle(_translate("PotentialSlopeFailureDialogBase", "Potential Slope Failure"))
        self.label_5.setText(_translate("PotentialSlopeFailureDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Slope failure angle:</p></body></html>"))
        self.pushButtonSave.setText(_translate("PotentialSlopeFailureDialogBase", "Select"))
        self.label_8.setText(_translate("PotentialSlopeFailureDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Number of search directions:</p></body></html>"))
        self.label_4.setText(_translate("PotentialSlopeFailureDialogBase", "Output folder:"))
        self.pushButton.setText(_translate("PotentialSlopeFailureDialogBase", "Close"))
        self.checkBoxIntoCanvas.setText(_translate("PotentialSlopeFailureDialogBase", "Add result to project"))
        self.runButton.setText(_translate("PotentialSlopeFailureDialogBase", "Run"))
        self.pushButtonHelp.setText(_translate("PotentialSlopeFailureDialogBase", "Help"))
        self.label_2.setText(_translate("PotentialSlopeFailureDialogBase", "Cohesive soils (1 = Cohesive Soil, 0 = Other):"))
        self.label.setText(_translate("PotentialSlopeFailureDialogBase", "Digital elevation model (DEM):"))

