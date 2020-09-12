import sys  # 导入系统

import pymysql
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from socket import *
from 主界面 import Ui_FormMain
from 区域数据统计 import Ui_FormPart
from 地区选择界面 import Ui_FormSelect
from 用户数据模块 import Ui_FormUser
from 输入界面 import Ui_FormInput
import pymysql as pymysql
import pyttsx3
import bgimag
import imag
ss = ''
db = pymysql.connect("127.0.0.1", "root", "Zmx131021", "Temperature")
cursor1 = db.cursor()
cursor2 = db.cursor()
cursor3 = db.cursor()
cursor4 = db.cursor()
cursor5 = db.cursor()
srecname = ''
srecID = ''
srecmax = 0.0
srecmin = 0.0
srecavg = 0.0

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
        ss = self.textEdit.text()
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
        ss=self.textEdit.toPlainText()
        srecID = self.textEdit.toPlainText()

        result = cursor1.execute("Select * from User_Info where UserID = " + ss)
        result2 = cursor2.execute("Select UserName from User_Info where UserID = " + ss)
        result3 = cursor3.execute("Select max(UserTemp) from User_Info where UserID = " + ss)
        result4 = cursor4.execute("Select min(UserTemp) from User_Info where UserID = " + ss)
        result5 = cursor5.execute("Select avg(UserTemp) from User_Info where UserID = " + ss)
        all_data = cursor1.fetchall()
        all_data2 = cursor2.fetchall()
        all_data3 = cursor3.fetchall()
        all_data4 = cursor4.fetchall()
        all_data5 = cursor5.fetchall()
        for data in all_data2:
            srecname = (str(all_data2[0])[1:5:1])
        #print(str(all_data[0])[1:5:1])
        for data in all_data:
            print(data)
        srecmax=float(str(all_data3)[2:6:1])
        srecmin=float(str(all_data4)[2:6:1])
        srecavg=float(str(all_data5)[2:7:1])
        print(srecname)
        print(srecID)
        print(srecmax)
        print(srecmin)
        print(srecavg)
        db.close()

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
        self.textBrowser_3.setText(srecname)
        self.textBrowser_2.setText(srecID)
        self.textBrowser_4.setText(str(srecmax))
        self.textBrowser_5.setText(str(srecmin))
        self.textBrowser_5.setText(str(srecavg))
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
        self.pushButton_35.clicked.connect(self.select_button35)
        #self.pushButton_45.clicked.connect(self.select_button45)
        self.textBrowser_2.setText(u"张开")
        self.textBrowser_3.setText(u"36")
        self.textBrowser_4.setText(u"2020-9-10-20：00")
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
    def select_button35(self):
        openvoice()
    #def select_button45(self):
        #while True:
            #success, frame = camera.read()
            #cv2.imshow('MyCamera', frame)
            #if cv2.waitKey(1) & 0xff == ord('q'):
                #break
        #cv2.destroyWindow('MyCamera')
        #camera.release()

def openvoice():
    voice = pyttsx3.init()
    voice.say('Hello world')
    voice.runAndWait()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())