# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'record_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(454, 425)
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 370, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.outVarsLabel = QtWidgets.QLabel(dialog)
        self.outVarsLabel.setGeometry(QtCore.QRect(10, 14, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outVarsLabel.setFont(font)
        self.outVarsLabel.setObjectName("outVarsLabel")
        self.outVarsLabel_2 = QtWidgets.QLabel(dialog)
        self.outVarsLabel_2.setGeometry(QtCore.QRect(10, 160, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outVarsLabel_2.setFont(font)
        self.outVarsLabel_2.setObjectName("outVarsLabel_2")
        self.avgRecEdit = QtWidgets.QLineEdit(dialog)
        self.avgRecEdit.setGeometry(QtCore.QRect(150, 210, 81, 21))
        self.avgRecEdit.setObjectName("avgRecEdit")
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(20, 210, 131, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(235, 210, 71, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 250, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 121, 21))
        self.label_4.setObjectName("label_4")
        self.filenameEdit = QtWidgets.QLineEdit(dialog)
        self.filenameEdit.setGeometry(QtCore.QRect(150, 250, 231, 21))
        self.filenameEdit.setObjectName("filenameEdit")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(380, 250, 31, 21))
        self.label_5.setObjectName("label_5")
        self.outLocEdit = QtWidgets.QLineEdit(dialog)
        self.outLocEdit.setGeometry(QtCore.QRect(20, 320, 391, 21))
        self.outLocEdit.setObjectName("outLocEdit")
        self.toolButton = QtWidgets.QToolButton(dialog)
        self.toolButton.setGeometry(QtCore.QRect(150, 290, 27, 22))
        self.toolButton.setObjectName("toolButton")
        self.widget = QtWidgets.QWidget(dialog)
        self.widget.setGeometry(QtCore.QRect(30, 50, 381, 88))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tempFBox = QtWidgets.QCheckBox(self.widget)
        self.tempFBox.setObjectName("tempFBox")
        self.gridLayout.addWidget(self.tempFBox, 0, 0, 1, 1)
        self.rhBox = QtWidgets.QCheckBox(self.widget)
        self.rhBox.setObjectName("rhBox")
        self.gridLayout.addWidget(self.rhBox, 0, 1, 1, 1)
        self.gamBox = QtWidgets.QCheckBox(self.widget)
        self.gamBox.setObjectName("gamBox")
        self.gridLayout.addWidget(self.gamBox, 0, 2, 1, 1)
        self.dpFBox = QtWidgets.QCheckBox(self.widget)
        self.dpFBox.setObjectName("dpFBox")
        self.gridLayout.addWidget(self.dpFBox, 1, 0, 1, 1)
        self.mmrBox = QtWidgets.QCheckBox(self.widget)
        self.mmrBox.setObjectName("mmrBox")
        self.gridLayout.addWidget(self.mmrBox, 1, 1, 1, 1)
        self.rhoBox = QtWidgets.QCheckBox(self.widget)
        self.rhoBox.setObjectName("rhoBox")
        self.gridLayout.addWidget(self.rhoBox, 1, 2, 1, 1)
        self.tempCBox = QtWidgets.QCheckBox(self.widget)
        self.tempCBox.setObjectName("tempCBox")
        self.gridLayout.addWidget(self.tempCBox, 2, 0, 1, 1)
        self.vcBox = QtWidgets.QCheckBox(self.widget)
        self.vcBox.setObjectName("vcBox")
        self.gridLayout.addWidget(self.vcBox, 2, 1, 1, 1)
        self.voltBox = QtWidgets.QCheckBox(self.widget)
        self.voltBox.setObjectName("voltBox")
        self.gridLayout.addWidget(self.voltBox, 2, 2, 1, 1)
        self.dpCBox = QtWidgets.QCheckBox(self.widget)
        self.dpCBox.setObjectName("dpCBox")
        self.gridLayout.addWidget(self.dpCBox, 3, 0, 1, 1)
        self.vpBox = QtWidgets.QCheckBox(self.widget)
        self.vpBox.setObjectName("vpBox")
        self.gridLayout.addWidget(self.vpBox, 3, 1, 1, 1)
        self.cntBox = QtWidgets.QCheckBox(self.widget)
        self.cntBox.setObjectName("cntBox")
        self.gridLayout.addWidget(self.cntBox, 3, 2, 1, 1)

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Setup Recording"))
        self.outVarsLabel.setText(_translate("dialog", "Select Output Variables"))
        self.outVarsLabel_2.setText(_translate("dialog", "Recording Options"))
        self.label.setText(_translate("dialog", "Averaged Recording:"))
        self.label_2.setText(_translate("dialog", "seconds"))
        self.label_3.setText(_translate("dialog", "Output Filename:"))
        self.label_4.setText(_translate("dialog", "Output Location:"))
        self.label_5.setText(_translate("dialog", ".csv"))
        self.toolButton.setText(_translate("dialog", "..."))
        self.tempFBox.setText(_translate("dialog", "Temperature °F"))
        self.rhBox.setText(_translate("dialog", "Relative Humidity"))
        self.gamBox.setText(_translate("dialog", "Gamma"))
        self.dpFBox.setText(_translate("dialog", "Dew Point °F"))
        self.mmrBox.setText(_translate("dialog", "Mass Mixing Ratio"))
        self.rhoBox.setText(_translate("dialog", "Density"))
        self.tempCBox.setText(_translate("dialog", "Temperature °C"))
        self.vcBox.setText(_translate("dialog", "Vapor Concentration"))
        self.voltBox.setText(_translate("dialog", "Voltage"))
        self.dpCBox.setText(_translate("dialog", "Dew Point °C"))
        self.vpBox.setText(_translate("dialog", "Vapor Pressure"))
        self.cntBox.setText(_translate("dialog", "Counts"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
