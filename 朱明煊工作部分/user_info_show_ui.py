# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_info_show.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_user_info_show(object):
    def setupUi(self, user_info_show):
        if not user_info_show.objectName():
            user_info_show.setObjectName(u"user_info_show")
        user_info_show.resize(800, 600)
        self.centralwidget = QWidget(user_info_show)
        self.centralwidget.setObjectName(u"centralwidget")
        self.ctrl_widgets = QWidget(self.centralwidget)
        self.ctrl_widgets.setObjectName(u"ctrl_widgets")
        self.ctrl_widgets.setGeometry(QRect(100, 100, 600, 400))
        self.verticalLayout = QVBoxLayout(self.ctrl_widgets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.user_info = QTextBrowser(self.ctrl_widgets)
        self.user_info.setObjectName(u"user_info")

        self.verticalLayout.addWidget(self.user_info)

        self.user_id = QLabel(self.ctrl_widgets)
        self.user_id.setObjectName(u"user_id")

        self.verticalLayout.addWidget(self.user_id)

        self.user_name = QLabel(self.ctrl_widgets)
        self.user_name.setObjectName(u"user_name")

        self.verticalLayout.addWidget(self.user_name)

        self.average_temperature = QLabel(self.ctrl_widgets)
        self.average_temperature.setObjectName(u"average_temperature")

        self.verticalLayout.addWidget(self.average_temperature)

        self.max_temperature = QLabel(self.ctrl_widgets)
        self.max_temperature.setObjectName(u"max_temperature")

        self.verticalLayout.addWidget(self.max_temperature)

        self.min_temperature = QLabel(self.ctrl_widgets)
        self.min_temperature.setObjectName(u"min_temperature")

        self.verticalLayout.addWidget(self.min_temperature)

        self.showChart = QPushButton(self.ctrl_widgets)
        self.showChart.setObjectName(u"showChart")

        self.verticalLayout.addWidget(self.showChart)

        user_info_show.setCentralWidget(self.centralwidget)

        self.retranslateUi(user_info_show)

        QMetaObject.connectSlotsByName(user_info_show)
    # setupUi

    def retranslateUi(self, user_info_show):
        user_info_show.setWindowTitle(QCoreApplication.translate("user_info_show", u"user info show", None))
        self.user_id.setText(QCoreApplication.translate("user_info_show", u"\u7528\u6237ID", None))
        self.user_name.setText(QCoreApplication.translate("user_info_show", u"\u7528\u6237\u59d3\u540d", None))
        self.average_temperature.setText(QCoreApplication.translate("user_info_show", u"\u5e73\u5747\u6e29\u5ea6", None))
        self.max_temperature.setText(QCoreApplication.translate("user_info_show", u"\u6700\u9ad8\u6e29\u5ea6", None))
        self.min_temperature.setText(QCoreApplication.translate("user_info_show", u"\u6700\u4f4e\u6e29\u5ea6", None))
        self.showChart.setText(QCoreApplication.translate("user_info_show", u"\u751f\u6210\u56fe\u8868", None))
    # retranslateUi

