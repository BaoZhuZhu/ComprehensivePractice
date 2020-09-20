"""
人脸识别
"""
import time
import datetime
from random import random



from Face.AppUi import Ui_Form
#import qdarkstyle
import PySide2 as PyQt5
# from PyQt5.QtCore import QTimer
import sys
# from PyQt5 import QtWidgets
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtWidgets import QMessageBox
import cv2
from Face.arcface import ArcFace
from advice import fun
from db_manager import UserDataAnalysis
from main import main_ui
from user_id_input import user_input_ui
from Face.module.face_process import FaceProcess
import threading
import os
from tempserver import A
import django
import random
from comprehensivePractice.models import UserInfo

HOST = ''
PORT = 8266  # 设置端口号
BUFSIZ = 1024
ADDRESS = (HOST, PORT)
demo = b"0"



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "model.settings")

django.setup()

def net_build_silent(address, callback):
    callback(A(address))

class MainWindow(PyQt5.QtWidgets.QWidget, Ui_Form):
    """
    构造函数，初始化,摄像头的显示不应堵塞主线程，因此需要QTimer类，每20ms刷新一次界面
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        self.timer = PyQt5.QtCore.QTimer()
        self.timer.timeout.connect(self.camshow)
        self.pushButton_1.clicked.connect(self.open_cam)
        self.pushButton_2.clicked.connect(self.close_cam)
        self.arcface = ArcFace(ArcFace.IMAGE_MODE)
        self.flag = 0  # 标志位，如果为1,说明人脸匹配成功 摄像头会自动关闭
        self.name = "None"
        self.sub_ui = []
        self.set_flots()
        self.guage = '1'
        self.a = None
        self.thread = threading.Thread(target=net_build_silent, args=(ADDRESS, self.net_build_callback))
        self.thread.start()

    def net_build_callback(self, a: A):
        self.a = a

    def set_flots(self):
        self.pre_loading.clicked.connect(self.open_cam)
        self.area_data.clicked.connect(self.to_area_select_ui)
        self.user_data.clicked.connect(self.to_user_input_ui)
        self.test_temp.clicked.connect(self.to_test_temp)
        self.open_voice.clicked.connect(self.to_open_voice)
        self.info_save.clicked.connect(self.to_info_save)

    def to_area_select_ui(self):
        self.subwidget = main_ui()
        self.sub_ui.append(self.subwidget)
        self.subwidget.show()
        pass

    def to_user_input_ui(self):
        self.subwidget = user_input_ui()
        self.sub_ui.append(self.subwidget)
        self.subwidget.show()
        pass

    def to_test_temp(self):
        self.guage = '0'
        if self.a is not None:
            temp = self.a.run(self.guage)
            self.user_temp.setText(str(temp))

    def to_open_voice(self):
        temp = float(self.user_temp.text())
        fun(temp)

    def to_info_save(self):
        userID = int(self.label_3.text()[3:13])

        #analyser = UserDataAnalysis(userID)
        userName = str(self.label_3.text()[0:3])
        userTemp = float(self.user_temp.text())
        st = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        now = datetime.datetime.strptime(st, '%Y-%m-%d %H:%M:%S')
        place = random.choice(["1","2","3"])
        print(str(userID)+' '+userName+' '+st+' '+str(userTemp)+ ' '+place)
        UserInfo(userID, userName,
                 userTemp, now,
                 place).save()
        self.user_temp.setText("保存成功")

    def camshow(self):
        """
        画面显示
        :return:
        """
        if self.flag:
            self.timer.stop()
            self.cap.release()
            return
        ret, self.img = self.cap.read()
        height, width, bytesPerComponent = self.img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB, self.img)
        QImg = PyQt5.QtGui.QImage(self.img.data, width, height, bytesPerLine, PyQt5.QtGui.QImage.Format_RGB888)
        pixmap = PyQt5.QtGui.QPixmap.fromImage(QImg)
        self.label_2.setPixmap(pixmap)  # opencv打开的图像显示在label上
    def open_cam(self):
        """
        打开摄像头
        :return:
        """
        self.flag = 0
        self.cap=cv2.VideoCapture(0)

        self.timer.start(20)
        self.label_3.setText("人脸识别中 ^*^")
        # self.pushButton_2.setEnabled(False)
        # self.pushButton.setEnabled(True)
        if self.cap.isOpened():
            #self.timer.start(20)  #也是相当于启动子线程，20ms刷新一次
            th=threading.Thread(target=self.campare)
            th.start()
        else:
            PyQt5.QtWidgets.QMessageBox.information(self, "警告", "摄像头打开失败！", QMessageBox.Ok | QMessageBox.Ok)

    def campare(self):
        """
        为了不堵塞主线程，开启子线程，进行人脸匹配
        """
        self.face_process = FaceProcess()
        self.face_process.add_features("FaceData")  # 提取人脸特征
        print("数据库中的人脸：" + str(self.face_process.features.keys()))

        while True:
            faces = self.arcface.detect_faces(self.img)  # 检测人脸

            # 仅当检测道人脸的时候才会提取特征
            if len(faces) > 0:

                # 防止提取到的特征无效，此处需要做异常处理
                try:
                    fea = self.arcface.extract_feature(self.img, faces[0])  # 提取特征

                    # fea = self.arcface.extract_feature(self.image, faces[index])  # 提取特征
                    for i in self.face_process.features.keys():
                        #print(i)
                        pro = self.arcface.compare_feature(fea, self.face_process.features[i])
                        if pro > 0.8:
                            print("匹配成功:%s" % i)
                            self.name = i  # 子线程和主线程通信
                            self.flag = 1  #
                            break
                except:
                    print("无效的人脸特征！")
            else:
                print("匹配失败！")
            if self.flag:
                self.label_3.setText(i)
                #QMessageBox.information(self, "tip", "恭喜您！刷脸成功！", QMessageBox.Ok | QMessageBox.Ok)
                break
    def close_cam(self):
        """
        关闭摄像头
        :return:
        """
        self.label_3.clear()
        self.label_2.clear()
        self.timer.stop()
        self.cap.release()
if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())






