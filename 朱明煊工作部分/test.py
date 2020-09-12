import sys  # 导入系统

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

from 主界面 import Ui_FormMain
from 区域数据统计 import Ui_FormPart
from 地区选择界面 import Ui_FormSelect
from 用户数据模块 import Ui_FormUser
from 输入界面 import Ui_FormInput

import bgimag
import imag

class SelectWindow(Ui_FormSelect, QWidget):
    def __init__(self):
        super(SelectWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('地区选择')
        self.pushButton1.clicked.connect(self.select_button1)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("/Users/zhumingxuan/Desktop/images/bg1.jpg")))
        self.setPalette(window_pale)
    def select_button1(self):
        self.hide()
        self.dia = PartWindow()
        self.dia.show()

class PartWindow(Ui_FormPart,QWidget):
    def __init__(self):
        super(PartWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('地区数据统计')
        self.pushButton2.clicked.connect(self.select_button2)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("/Users/zhumingxuan/Desktop/images/bg1.jpg")))
        self.setPalette(window_pale)
    def select_button2(self):
        self.hide()
        self.dia = MainWindow()
        self.dia.show()

class InputWindow(Ui_FormInput,QWidget):
    def __init__(self):
        super(InputWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('用户账号输入')
        self.pushButton3.clicked.connect(self.select_button3)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("/Users/zhumingxuan/Desktop/images/bg1.jpg")))
        self.setPalette(window_pale)
    def select_button3(self):
        self.hide()
        self.dia = UserWindow()
        self.dia.show()

class UserWindow(Ui_FormUser,QWidget):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('用户数据显示')
        #self.pushButton4.clicked.connect(self.select_button4)
        self.pushButton_24.clicked.connect(self.select_button24)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("/Users/zhumingxuan/Desktop/images/bg1.jpg")))
        self.setPalette(window_pale)
    def select_button24(self):
        self.hide()
        self.dia = MainWindow()
        self.dia.show()

class MainWindow(Ui_FormMain,QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('主界面')
        self.pushButton5.clicked.connect(self.select_button5)
        self.pushButton_25.clicked.connect(self.select_button25)
        #self.pushButton_35.clicked.connect(self.select_button35)
        window_pale = QtGui.QPalette()
        window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("/Users/zhumingxuan/Desktop/images/bg1.jpg")))
        self.setPalette(window_pale)
    def select_button5(self):
        self.hide()
        self.dia = InputWindow()
        self.dia.show()
    def select_button25(self):
        self.hide()
        self.dia = SelectWindow()
        self.dia.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())