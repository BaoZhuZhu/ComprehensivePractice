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

import main_rc

class Ui_userDataVisual(object):
    def setupUi(self, userDataVisual):
        if not userDataVisual.objectName():
            userDataVisual.setObjectName(u"userDataVisual")
        userDataVisual.resize(800, 600)
        userDataVisual.setAutoFillBackground(False)
        self.centralwidget = QWidget(userDataVisual)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(True)
        self.ctrl_widget = QWidget(self.centralwidget)
        self.ctrl_widget.setObjectName(u"ctrl_widget")
        self.ctrl_widget.setGeometry(QRect(100, 400, 200, 100))
        self.verticalLayout = QVBoxLayout(self.ctrl_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.area_risk = QLabel(self.ctrl_widget)
        self.area_risk.setObjectName(u"area_risk")

        self.verticalLayout.addWidget(self.area_risk)

        self.people_count = QLabel(self.ctrl_widget)
        self.people_count.setObjectName(u"people_count")

        self.verticalLayout.addWidget(self.people_count)

        self.average_temperature = QLabel(self.ctrl_widget)
        self.average_temperature.setObjectName(u"average_temperature")

        self.verticalLayout.addWidget(self.average_temperature)

        userDataVisual.setCentralWidget(self.centralwidget)

        self.retranslateUi(userDataVisual)

        QMetaObject.connectSlotsByName(userDataVisual)
    # setupUi

    def retranslateUi(self, userDataVisual):
        userDataVisual.setWindowTitle(QCoreApplication.translate("userDataVisual", u"userDataVisual", None))
        self.area_risk.setText(QCoreApplication.translate("userDataVisual", u"\u8be5\u5730\u533a\u98ce\u9669\uff1a", None))
        self.people_count.setText(QCoreApplication.translate("userDataVisual", u"\u603b\u4eba\u6570\uff1a", None))
        self.average_temperature.setText(QCoreApplication.translate("userDataVisual", u"\u5e73\u5747\u6e29\u5ea6\uff1a", None))
    # retranslateUi

