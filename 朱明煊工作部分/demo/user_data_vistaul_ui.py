# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_data_visual.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys


class Ui_userDataVisual(object):
    def setupUi(self, userDataVisual):
        if not userDataVisual.objectName():
            userDataVisual.setObjectName(u"userDataVisual")
        userDataVisual.resize(878, 596)
        self.back_button = QPushButton(userDataVisual)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(700, 520, 91, 41))

        self.retranslateUi(userDataVisual)

        QMetaObject.connectSlotsByName(userDataVisual)
    # setupUi

    def retranslateUi(self, userDataVisual):
        userDataVisual.setWindowTitle(QCoreApplication.translate("userDataVisual", u"Form", None))
        self.back_button.setText(QCoreApplication.translate("userDataVisual", u"\u56de\u5230\u4e3b\u754c\u9762", None))
    # retranslateUi
