# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(472, 299)
        self.label2 = QtWidgets.QLabel(dialog)
        self.label2.setGeometry(QtCore.QRect(30, 137, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(dialog)
        self.label1.setGeometry(QtCore.QRect(30, 26, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.buttonBox = QtWidgets.QDialogButtonBox(dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 341, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label3 = QtWidgets.QLabel(dialog)
        self.label3.setGeometry(QtCore.QRect(30, 53, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(dialog)
        self.label4.setGeometry(QtCore.QRect(30, 162, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.lineLC = QtWidgets.QLineEdit(dialog)
        self.lineLC.setGeometry(QtCore.QRect(120, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineLC.setFont(font)
        self.lineLC.setText("")
        self.lineLC.setPlaceholderText("")
        self.lineLC.setObjectName("lineLC")
        self.lineWVSS = QtWidgets.QLineEdit(dialog)
        self.lineWVSS.setGeometry(QtCore.QRect(120, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineWVSS.setFont(font)
        self.lineWVSS.setText("")
        self.lineWVSS.setPlaceholderText("")
        self.lineWVSS.setClearButtonEnabled(False)
        self.lineWVSS.setObjectName("lineWVSS")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Port Configuration"))
        self.label2.setText(_translate("dialog", "Water Vapor Monitor System"))
        self.label1.setText(_translate("dialog", "DataQ DI-145"))
        self.label3.setText(_translate("dialog", "COM port: "))
        self.label4.setText(_translate("dialog", "COM port: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
