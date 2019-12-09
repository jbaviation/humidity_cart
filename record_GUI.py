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
        self.outVarsLabel.setGeometry(QtCore.QRect(20, 14, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outVarsLabel.setFont(font)
        self.outVarsLabel.setObjectName("outVarsLabel")
        self.dpBox = QtWidgets.QCheckBox(dialog)
        self.dpBox.setGeometry(QtCore.QRect(30, 50, 131, 17))
        self.dpBox.setObjectName("dpBox")
        self.mmrBox = QtWidgets.QCheckBox(dialog)
        self.mmrBox.setGeometry(QtCore.QRect(30, 90, 131, 17))
        self.mmrBox.setObjectName("mmrBox")
        self.rhBox = QtWidgets.QCheckBox(dialog)
        self.rhBox.setGeometry(QtCore.QRect(30, 70, 131, 17))
        self.rhBox.setObjectName("rhBox")
        self.vcBox = QtWidgets.QCheckBox(dialog)
        self.vcBox.setGeometry(QtCore.QRect(30, 110, 131, 17))
        self.vcBox.setObjectName("vcBox")
        self.gamBox = QtWidgets.QCheckBox(dialog)
        self.gamBox.setGeometry(QtCore.QRect(190, 50, 131, 17))
        self.gamBox.setObjectName("gamBox")
        self.rhoBox = QtWidgets.QCheckBox(dialog)
        self.rhoBox.setGeometry(QtCore.QRect(190, 70, 131, 17))
        self.rhoBox.setObjectName("rhoBox")
        self.voltBox = QtWidgets.QCheckBox(dialog)
        self.voltBox.setGeometry(QtCore.QRect(190, 90, 131, 17))
        self.voltBox.setObjectName("voltBox")
        self.cntBox = QtWidgets.QCheckBox(dialog)
        self.cntBox.setGeometry(QtCore.QRect(190, 110, 131, 17))
        self.cntBox.setObjectName("cntBox")
        self.outVarsLabel_2 = QtWidgets.QLabel(dialog)
        self.outVarsLabel_2.setGeometry(QtCore.QRect(20, 160, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.outVarsLabel_2.setFont(font)
        self.outVarsLabel_2.setObjectName("outVarsLabel_2")

        self.retranslateUi(dialog)
        self.buttonBox.accepted.connect(dialog.accept)
        self.buttonBox.rejected.connect(dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Setup Recording"))
        self.outVarsLabel.setText(_translate("dialog", "Select Output Variables"))
        self.dpBox.setText(_translate("dialog", "Dew Point"))
        self.mmrBox.setText(_translate("dialog", "Mass Mixing Ratio"))
        self.rhBox.setText(_translate("dialog", "Relative Humidity"))
        self.vcBox.setText(_translate("dialog", "Vapor Concentration"))
        self.gamBox.setText(_translate("dialog", "Gamma"))
        self.rhoBox.setText(_translate("dialog", "Density"))
        self.voltBox.setText(_translate("dialog", "Voltage"))
        self.cntBox.setText(_translate("dialog", "Counts"))
        self.outVarsLabel_2.setText(_translate("dialog", "Recording Style"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
