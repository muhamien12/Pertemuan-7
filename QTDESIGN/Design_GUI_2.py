# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Design_GUI_2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(407, 306)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 70, 181, 16))
        self.label.setObjectName("label")
        self.Halo = QtWidgets.QPushButton(Form)
        self.Halo.setGeometry(QtCore.QRect(110, 150, 75, 23))
        self.Halo.setObjectName("Halo")
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(200, 150, 75, 23))
        self.Clear.setObjectName("Clear")
        self.Exit = QtWidgets.QPushButton(Form)
        self.Exit.setGeometry(QtCore.QRect(150, 200, 75, 23))
        self.Exit.setObjectName("Exit")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(112, 110, 151, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Masukan Nama Anda</span></p></body></html>"))
        self.Halo.setText(_translate("Form", "Halo"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.Exit.setText(_translate("Form", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

