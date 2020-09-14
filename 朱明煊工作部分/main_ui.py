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

import main_rc

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        main.setLayoutDirection(Qt.LeftToRight)
        main.setAutoFillBackground(False)
        main.setStyleSheet(u"")
        self.bg_img = QLabel(main)
        self.bg_img.setObjectName(u"bg_img")
        self.bg_img.setEnabled(True)
        self.bg_img.setGeometry(QRect(0, 0, 800, 600))
        sizePolicy.setHeightForWidth(self.bg_img.sizePolicy().hasHeightForWidth())
        self.bg_img.setSizePolicy(sizePolicy)
        self.bg_img.setPixmap(QPixmap(u":/bg.jpg"))
        self.bg_img.setScaledContents(True)
        self.bg_img.setAlignment(Qt.AlignCenter)
        self.ctrl_widgets = QWidget(main)
        self.ctrl_widgets.setObjectName(u"ctrl_widgets")
        self.ctrl_widgets.setGeometry(QRect(0, 0, 400, 600))
        self.verticalLayout = QVBoxLayout(self.ctrl_widgets)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.time_select = QComboBox(self.ctrl_widgets)
        self.time_select.addItem("")
        self.time_select.addItem("")
        self.time_select.addItem("")
        self.time_select.addItem("")
        self.time_select.setObjectName(u"time_select")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.time_select.sizePolicy().hasHeightForWidth())
        self.time_select.setSizePolicy(sizePolicy1)
        self.time_select.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.time_select)

        self.area_select = QComboBox(self.ctrl_widgets)
        self.area_select.addItem("")
        self.area_select.addItem("")
        self.area_select.addItem("")
        self.area_select.addItem("")
        self.area_select.setObjectName(u"area_select")
        sizePolicy1.setHeightForWidth(self.area_select.sizePolicy().hasHeightForWidth())
        self.area_select.setSizePolicy(sizePolicy1)
        self.area_select.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.area_select)

        self.push_button = QPushButton(self.ctrl_widgets)
        self.push_button.setObjectName(u"push_button")
        self.push_button.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.push_button.sizePolicy().hasHeightForWidth())
        self.push_button.setSizePolicy(sizePolicy2)
        self.push_button.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.push_button)

        self.bg_img.raise_()
        self.ctrl_widgets.raise_()

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main_ui", None))
        self.bg_img.setText("")
        self.time_select.setItemText(0, QCoreApplication.translate("main", u"\u9009\u62e9\u65f6\u95f4", None))
        self.time_select.setItemText(1, QCoreApplication.translate("main", u"time1", None))
        self.time_select.setItemText(2, QCoreApplication.translate("main", u"time2", None))
        self.time_select.setItemText(3, QCoreApplication.translate("main", u"time3", None))

        self.area_select.setItemText(0, QCoreApplication.translate("main", u"\u9009\u62e9\u5730\u533a", None))
        self.area_select.setItemText(1, QCoreApplication.translate("main", u"\u5730\u533a1", None))
        self.area_select.setItemText(2, QCoreApplication.translate("main", u"\u5730\u533a2", None))
        self.area_select.setItemText(3, QCoreApplication.translate("main", u"\u5730\u533a3", None))

        self.push_button.setText(QCoreApplication.translate("main", u"\u786e\u5b9a", None))
    # retranslateUi

