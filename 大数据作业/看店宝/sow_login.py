from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
import logic
import sys
import window_main1

class Main(QMainWindow, window_main1.Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

class LoginDialog(QMainWindow, logic.Ui_MainWindow):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.setupUi(self)
        self.mBtnCancel.clicked.connect(self.onCancleClicked)
        self.mBtnLogin.clicked.connect(self.onLoginClicked)

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