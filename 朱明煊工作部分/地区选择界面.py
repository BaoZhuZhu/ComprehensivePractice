# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '地区选择界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import bgimag
import imag


class Ui_FormSelect(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 395)
        #Form.setStyleSheet("background-image: url(:/imgTest/bg1.jpg);")
        self.pushButton1 = QtWidgets.QPushButton(Form)
        self.pushButton1.setGeometry(QtCore.QRect(270, 300, 112, 32))
        font = QtGui.QFont()
        font.setFamily("Wawati SC")
        font.setPointSize(14)
        self.pushButton1.setFont(font)
        self.pushButton1.setMouseTracking(True)
        #self.pushButton1.setStyleSheet("background-image: url(:/Test/bgimg/bg3.jpeg);")
        self.pushButton1.setObjectName("pushButton1")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 40, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label.setFont(font)
        #self.label.setStyleSheet("background-image: url(:/Test/bgimg/bg3.jpeg);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(240, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(14)
        self.label_2.setFont(font)
        #self.label_2.setStyleSheet("background-image: url(:/Test/bgimg/bg3.jpeg);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(240, 80, 170, 32))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        self.comboBox.setFont(font)
        #self.comboBox.setStyleSheet("background-image: url(:/Test/bgimg/bg3.jpeg);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(240, 240, 170, 32))
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        self.comboBox_2.setFont(font)
        #self.comboBox_2.setStyleSheet("background-image: url(:/Test/bgimg/bg3.jpeg);")
        self.comboBox_2.setObjectName("comboBox_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton1.setText(_translate("Form", "确认"))
        self.label.setText(_translate("Form", "请选择您想查看的地区"))
        self.label_2.setText(_translate("Form", "请选择您想查看的时段"))

