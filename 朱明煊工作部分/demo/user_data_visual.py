import sys

from PySide2.QtWidgets import QWidget, QApplication

from demo.user_data_vistaul_ui import Ui_userDataVisual


class userDataVisual(Ui_userDataVisual, QWidget):

    def __init__(self):
        super(userDataVisual, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication()
    widget = userDataVisual()
    widget.show()
    sys.exit(app.exec_())