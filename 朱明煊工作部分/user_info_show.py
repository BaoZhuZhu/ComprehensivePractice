import sys

import PySide2
from PySide2.QtCore import QPoint, Qt, QRect
from PySide2.QtGui import QPainter, QBrush, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow
import matplotlib.pyplot as plt
from common import times
from db_manager import UserDataAnalysis
from user_info_show_ui import Ui_user_info_show
from PySide2.QtCharts import QtCharts
import main_rc

class userInfoVisual(Ui_user_info_show, QMainWindow):

    def __init__(self, userID):
        super(userInfoVisual, self).__init__()
        self.setupUi(self)
        self.bg_pixmap = QPixmap(u":/bg.jpg")
        self.org_bg_pixmap = QPixmap(u":/bg.jpg")

        self.__userID = userID
        analyser = UserDataAnalysis(userID)

        self.info = analyser.user_info
        self.temp = analyser.user_temp
        self.time = analyser.user_time
        self.user_id.setText(
            "用户ID:{}".format(str(userID)))
        self.user_name.setText(
            "用户姓名:{}".format(str(analyser.user_name)))
        self.average_temperature.setText(
            "平均温度:{}".format(round(analyser.average_temperature,2)))
        self.max_temperature.setText(
            "最高温度:{}".format(round(analyser.max_temperature,2)))
        self.min_temperature.setText(
            "最低温度:{}".format(round(analyser.min_temperature,2)))
        self.user_info.setText(
            "信息:{}".format(str(self.info)))
        self.set_slots()

        self.lineSeries = QtCharts.QLineSeries()
        self.lineSeries.setName("time-temp")
        self.data_set = []
        for i, t in enumerate(self.temp):
            self.data_set.append(QPoint(i, t))
        self.lineSeries.append(self.data_set)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.lineSeries)
        self.chart.setTitle("用户个人温度变化曲线图")

        self.axisX = QtCharts.QCategoryAxis()
        for i, t in enumerate(self.time):
            self.axisX.append(t, i)
        self.chart.setAxisX(self.axisX, self.lineSeries)

        self.axisY = QtCharts.QValueAxis()
        self.chart.setAxisY(self.axisY, self.lineSeries)
        self.axisY.setRange(35, 39)

        self.chart.axisY().setTitleText("体温")
        self.chart.axisX().setTitleText("时间")

        self.chart.legend().setVisible(False)
        self.chartView = QtCharts.QChartView(self.chart, self.centralwidget)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setVisible(False)

    def set_slots(self):
        self.showChart.clicked.connect(self.get_plots)

    def get_plots(self):
        print(self.temp)
        print(self.time)
        self.chartView.setVisible(True)
        self.reRender()

    def reRender(self):
        self.ctrl_widgets.setGeometry(QRect(self.size().width() * 0.1,
                                            0,
                                            self.size().width() * 0.25,
                                            self.size().height()))
        self.chartView.setGeometry(QRect(self.size().width() * 0.4,
                                         0,
                                         self.size().width() * 0.5,
                                         self.size().height()))


    def resizeEvent(self, event: PySide2.QtGui.QResizeEvent):
        super().resizeEvent(event)
        self.setBackgroundImage()

        if self.chartView.isVisible():
            self.reRender()
        else:
            self.ctrl_widgets.setGeometry(QRect(self.size().width() * 0.25,
                                                0,
                                                self.size().width() * 0.5,
                                                self.size().height()))

    def setBackgroundImage(self):
        self.bg_pixmap = self.org_bg_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        palette = self.palette()
        palette.setBrush(self.backgroundRole(),
                  QBrush(self.bg_pixmap))
        self.setPalette(palette)
