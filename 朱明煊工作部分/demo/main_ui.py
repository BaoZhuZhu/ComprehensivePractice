# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        main.setAutoFillBackground(False)
        main.setStyleSheet(u"")
        self.layoutWidget = QWidget(main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(240, 90, 331, 321))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.area_select = QComboBox(self.layoutWidget)
        self.area_select.addItem("")
        self.area_select.addItem("")
        self.area_select.addItem("")
        self.area_select.addItem("")
        self.area_select.setObjectName(u"area_select")

        self.verticalLayout.addWidget(self.area_select)

        self.time_select = QComboBox(self.layoutWidget)
        self.time_select.addItem("")
        self.time_select.addItem("")
        self.time_select.addItem("")
        self.time_select.addItem("")
        self.time_select.setObjectName(u"time_select")

        self.verticalLayout.addWidget(self.time_select)

        self.push_button = QPushButton(self.layoutWidget)
        self.push_button.setObjectName(u"push_button")

        self.verticalLayout.addWidget(self.push_button)

        self.push_button.raise_()
        self.time_select.raise_()
        self.area_select.raise_()
        self.bg_view = QTextEdit(main)
        self.bg_view.setObjectName(u"bg_view")
        self.bg_view.setGeometry(QRect(0, 0, 801, 601))
        self.bg_view.setStyleSheet(u"background-image: url(:/bg1.png);")
        self.bg_view.raise_()
        self.layoutWidget.raise_()

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main_ui", None))
        self.area_select.setItemText(0, QCoreApplication.translate("main", u"\u9009\u62e9\u5730\u533a", None))
        self.area_select.setItemText(1, QCoreApplication.translate("main", u"\u5730\u533a1", None))
        self.area_select.setItemText(2, QCoreApplication.translate("main", u"\u5730\u533a2", None))
        self.area_select.setItemText(3, QCoreApplication.translate("main", u"\u5730\u533a3", None))

        self.time_select.setItemText(0, QCoreApplication.translate("main", u"\u9009\u62e9\u65f6\u95f4", None))
        self.time_select.setItemText(1, QCoreApplication.translate("main", u"time1", None))
        self.time_select.setItemText(2, QCoreApplication.translate("main", u"time2", None))
        self.time_select.setItemText(3, QCoreApplication.translate("main", u"time3", None))

        self.push_button.setText(QCoreApplication.translate("main", u"\u786e\u5b9a", None))
    # retranslateUi

