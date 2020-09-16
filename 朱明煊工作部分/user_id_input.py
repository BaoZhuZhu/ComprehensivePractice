import sys

import PySide2
from PySide2.QtCore import QRect
from PySide2.QtWidgets import QApplication, QWidget

from user_info_show import userInfoVisual
# from common import areas, times
from user_input_ui import Ui_userInput


class user_input_ui(Ui_userInput,QWidget):
    def __init__(self):
        super(user_input_ui, self).__init__()
        self.setupUi(self)
        self.sub_ui = []
        self.set_slots()

    def set_slots(self):
        self.push_button.clicked.connect(self.to_user_info_show_ui)

    def to_user_info_show_ui(self):
        userID = int(self.input.toPlainText())
        self.subwidget = userInfoVisual(userID)
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
    widget = user_input_ui()
    widget.show()
    sys.exit(app.exec_())