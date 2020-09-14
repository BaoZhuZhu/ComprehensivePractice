# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_data_visual.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import main_rc


class Ui_userInput(object):
    def setupUi(self, userinput):
        if not userinput.objectName():
            userinput.setObjectName(u"userinput")
        userinput.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(userinput.sizePolicy().hasHeightForWidth())
        userinput.setLayoutDirection(Qt.LeftToRight)
        userinput.setAutoFillBackground(False)
        userinput.setStyleSheet(u"")
        self.bg_img = QLabel(userinput)
        self.bg_img.setObjectName(u"bg_img")
        self.bg_img.setEnabled(True)
        self.bg_img.setGeometry(QRect(0, 0, 800, 600))
        sizePolicy.setHeightForWidth(self.bg_img.sizePolicy().hasHeightForWidth())
        self.bg_img.setSizePolicy(sizePolicy)
        self.bg_img.setPixmap(QPixmap(u":/bg.jpg"))
        self.bg_img.setScaledContents(True)
        self.bg_img.setAlignment(Qt.AlignCenter)
        self.ctrl_widgets = QWidget(userinput)
        self.ctrl_widgets.setObjectName(u"ctrl_widgets")
        self.ctrl_widgets.setGeometry(QRect(0, 0, 400, 600))
        self.input = QTextEdit(userinput)
        self.input.setObjectName(u"input")
        #sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #sizePolicy1.setHorizontalStretch(0)
        #sizePolicy1.setVerticalStretch(0)
        #sizePolicy1.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        #self.input.setSizePolicy(sizePolicy1)
        #self.input.setAutoFillBackground(True)


        self.push_button = QPushButton(self.ctrl_widgets)
        self.push_button.setObjectName(u"push_button")
        self.push_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.push_button.sizePolicy().hasHeightForWidth())
        self.push_button.setSizePolicy(sizePolicy2)
        self.push_button.setAutoFillBackground(True)


        self.verticalLayout = QVBoxLayout(self.ctrl_widgets)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.remind = QtWidgets.QLabel(self.ctrl_widgets)
        font = QtGui.QFont()
        font.setFamily("Yuppy SC")
        font.setPointSize(18)
        self.remind.setFont(font)
        self.remind.setObjectName(u"remind")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.remind.sizePolicy().hasHeightForWidth())
        self.remind.setSizePolicy(sizePolicy1)
        self.remind.setAutoFillBackground(True)
        self.input.setFixedSize(400,30)
        self.verticalLayout.addWidget(self.remind)
        self.verticalLayout.addWidget(self.input)
        self.verticalLayout.addWidget(self.push_button)
        self.bg_img.raise_()
        self.ctrl_widgets.raise_()

        self.retranslateUi(userinput)
        QtCore.QMetaObject.connectSlotsByName(userinput)

    def retranslateUi(self, userinput):
        _translate = QtCore.QCoreApplication.translate
        userinput.setWindowTitle(_translate("userinput", u"userinput_ui"))
        self.remind.setText(_translate("userinput", "请输入您想查询的用户ID"))
        self.push_button.setText(_translate("userinput", "确认"))

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = QWidget()
	w = Ui_userInput()
	w.setupUi(form)
	form.show()
	sys.exit(app.exec_())
