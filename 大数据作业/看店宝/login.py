# coding:utf-8

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import ui_login
import sys
import window_main

from PyQt5.QtGui import QMouseEvent
from PyQt5 import Qt

import ui_login

class Main(QMainWindow, window_main.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

class LoginDialog(QMainWindow, ui_login.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setWindowFlag(Qt.Qt.FramelessWindowHint)  # 隐藏窗口标题栏
        self.mDragWindow = False
        self.mMousePoint = []
        self.mBtnCancel.clicked.connect(self.onCancleClicked)
        self.mBtnLogin.clicked.connect(self.onLoginClicked)

    def mouseMoveEvent(self, event):
        e = QMouseEvent(event)
        if self.mDragWindow:
            self.move(e.globalPos() - self.mMousePoint)
            e.accept()

    def mousePressEvent(self, event):
        e = QMouseEvent(event)
        if e.button() == Qt.Qt.LeftButton:
            self.mMousePoint = e.globalPos() - self.pos()
            self.mDragWindow = True
            e.accept()

    def mouseReleaseEvent(self, event):
        self.mDragWindow = False

    def onLoginClicked(self):
        name = self.mTextUserName.text()
        passwd = self.mTextPassword.text()
        QMessageBox.information(None, "登录提示", "用户名：" + name + "密码：" + passwd, QMessageBox.Ok, QMessageBox.Ok)
        self.close()

        self.main = Main()
        # 显示主窗体
        self.main.show()

    def onCancleClicked(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginDialog()
    win.show()

    sys.exit(app.exec_())
