import sys

from PySide2.QtWidgets import QApplication, QWidget

from demo.main_ui import Ui_main
from demo.user_data_visual import userDataVisual


class main_ui(Ui_main,QWidget):
    def __init__(self):
        super(main_ui, self).__init__()
        self.setupUi(self)
        self.sub_ui = []
        self.set_slots()

    def set_slots(self):
        self.push_button.clicked.connect(self.to_user_data_visual_ui)

    def to_user_data_visual_ui(self):
        self.subwidget = userDataVisual()
        self.sub_ui.append(self.subwidget)
        self.subwidget.show()


if __name__ == "__main__":
    app = QApplication([])
    widget = main_ui()
    widget.show()
    sys.exit(app.exec_())
