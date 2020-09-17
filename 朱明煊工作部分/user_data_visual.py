import sys

import PySide2
from PySide2.QtCore import QPoint, Qt, QRect
from PySide2.QtGui import QPainter, QBrush, QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow

from common import times,days
from db_manager import DataAnalysis
from user_data_visual_ui import Ui_userDataVisual
from PySide2.QtCharts import QtCharts
import main_rc

class userDataVisual(Ui_userDataVisual, QMainWindow):

    def __init__(self, dayIndex,timeIndex, areaIndex):
        super(userDataVisual, self).__init__()
        self.setupUi(self)
        self.bg_pixmap = QPixmap(u":/bg.jpg")
        self.org_bg_pixmap = QPixmap(u":/bg.jpg")

        self.__dayIndex = dayIndex
        self.__timeIndex = timeIndex
        self.__areaIndex = areaIndex

        start_time, end_time = self.getTimeRange()
        month_time, day_time = self.getDay()
        analyser = DataAnalysis(start_time, end_time, month_time,day_time,self.__areaIndex)

        self.average_temperature.setText(
            "平均温度：{}".format(round(analyser.average_temperature, 2)))
        self.people_count.setText("总人数：{}".format(analyser.people_count))
        self.area_risk.setText(
            "该地区风险：{}".format("低" if analyser.area_risk_level == 0 else "高"))

        categories_count = analyser.get_people_count_by_temperature_range(35, 38.5, 0.5)
        self.set0 = QtCharts.QBarSet("temp-count")
        self.set0.append(categories_count)
        self.barSeries = QtCharts.QBarSeries()
        self.barSeries.append(self.set0)

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.barSeries)
        self.chart.setTitle("区域时段统计图")

        self.categories = ["35以下"]
        self.categories.extend(
            [str(i * 0.5 + 35) for i in range(len(categories_count) - 2)])
        self.categories.extend(["38.5以上"])
        self.axisX = QtCharts.QBarCategoryAxis()
        self.axisX.append(self.categories)
        self.chart.setAxisX(self.axisX, self.barSeries)
        self.axisX.setRange("35以下", "38.5以上")

        self.axisY = QtCharts.QValueAxis()
        self.chart.setAxisY(self.axisY, self.barSeries)
        self.axisY.setRange(min(categories_count), max(categories_count))

        self.chart.axisY().setTitleText("人数")
        self.chart.axisX().setTitleText("体温")
        self.chart.legend().setVisible(False)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart, self.centralwidget)
        self.chartView.setRenderHint(QPainter.Antialiasing)
        self.chartView.setGeometry(QRect(50, 50, 600, 450))



    def resizeEvent(self, event: PySide2.QtGui.QResizeEvent):
        super().resizeEvent(event)
        size = self.size()
        self.setBackgroundImage()
        self.chartView.setGeometry(QRect(size.width() * 0.05, size.height() * 0.1,
                                         size.width() * 0.6, size.height() * 0.6))
        self.ctrl_widget.setGeometry(QRect(size.width() * 0.05, size.height() * 0.7,
                                         size.width() / 4, size.height() / 6))

    def setBackgroundImage(self):
        self.bg_pixmap = self.org_bg_pixmap.scaled(self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

        palette = self.palette()
        palette.setBrush(self.backgroundRole(),
                  QBrush(self.bg_pixmap))
        self.setPalette(palette)

    def getTimeRange(self):
        start_time, end_time = times[self.__timeIndex-1].split("-")
        start_time = int(start_time.split(":")[0])
        end_time = int(end_time.split(":")[0])
        return [start_time, end_time]

    def getDay(self):
        day_time = days[self.__dayIndex-1]
        month = int(day_time.split("-")[0])
        day = int(day_time.split("-")[1])
        return  [month,day]