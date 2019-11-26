# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 299)
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(30, 110, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(30, 7, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 240, 341, 32))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(30, 53, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label3.setFont(font)
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(Dialog)
        self.label4.setGeometry(QtCore.QRect(30, 162, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label4.setFont(font)
        self.label4.setObjectName("label4")
        self.lineLC = QtWidgets.QLineEdit(Dialog)
        self.lineLC.setGeometry(QtCore.QRect(120, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineLC.setFont(font)
        self.lineLC.setText("")
        self.lineLC.setPlaceholderText("")
        self.lineLC.setObjectName("lineLC")
        self.lineWVSS = QtWidgets.QLineEdit(Dialog)
        self.lineWVSS.setGeometry(QtCore.QRect(120, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineWVSS.setFont(font)
        self.lineWVSS.setText("")
        self.lineWVSS.setPlaceholderText("")
        self.lineWVSS.setClearButtonEnabled(False)
        self.lineWVSS.setObjectName("lineWVSS")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label2.setText(_translate("Dialog", "Water Vapor Monitor System"))
        self.label1.setText(_translate("Dialog", "DataQ DI-145"))
        self.label3.setText(_translate("Dialog", "COM port: "))
        self.label4.setText(_translate("Dialog", "COM port: "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
