import sys

import PySide2
from PySide2.QtCore import QRect
from PySide2.QtWidgets import QApplication, QWidget

from common import areas, times , days
from main_ui import Ui_main
from user_data_visual import userDataVisual


class main_ui(Ui_main,QWidget):
    def __init__(self):
        super(main_ui, self).__init__()
        self.setupUi(self)
        self.sub_ui = []
        self.set_slots()
        for i, day_str in enumerate(days):
            self.day_select.setItemText(i+1, day_str)

        for i, area_name in enumerate(areas):
            self.area_select.setItemText(i+1, area_name)

        for i, time_str in enumerate(times):
            self.time_select.setItemText(i+1, time_str)

    def set_slots(self):
        self.push_button.clicked.connect(self.to_user_data_visual_ui)

    def to_user_data_visual_ui(self):
        dayIndex = self.day_select.currentIndex()
        timeIndex = self.time_select.currentIndex()
        areaIndex = self.area_select.currentIndex()
        dayIndex = 1 if dayIndex == 0 else dayIndex
        timeIndex = 1 if timeIndex == 0 else timeIndex
        areaIndex = 1 if areaIndex == 0 else areaIndex

        self.subwidget = userDataVisual(dayIndex,timeIndex, areaIndex)
        self.sub_ui.append(self.subwidget)

        self.subwidget.show()

    def resizeEvent(self, event: PySide2.QtGui.QResizeEvent):
        super().resizeEvent(event)
        self.bg_img.resize(self.size())
        self.ctrl_widgets.setGeometry(QRect(self.size().width() * 0.25,
                                            0,
                                            self.size().width() * 0.5,
                                            self.size().height()))


if __name__ == "__main__":
    app = QApplication([])
    widget = main_ui()
    widget.show()
    sys.exit(app.exec_())
