import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from cjl import test_rc


class SecondUI(QWidget):

    def __init__(self):
        super(SecondUI, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle("正在获取财务数据")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 80, 181, 91))
        self.label.setText("Second UI")


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

        self.pushButton.clicked.connect(self.mess)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 870)
        MainWindow.setStyleSheet("border-image: url(:/newPrefix/img/1.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton.setGeometry(QtCore.QRect(160, 190, 100, 50))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.setGeometry(QtCore.QRect(160, 290, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3.setGeometry(QtCore.QRect(160, 390, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4.setGeometry(QtCore.QRect(440, 190, 100, 50))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5.setGeometry(QtCore.QRect(440, 290, 100, 50))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6.setGeometry(QtCore.QRect(440, 400, 100, 50))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "获取财务数据"))
        self.pushButton_2.setText(_translate("MainWindow", "*********"))
        self.pushButton_3.setText(_translate("MainWindow", "*********"))
        self.pushButton_4.setText(_translate("MainWindow", "*********"))
        self.pushButton_5.setText(_translate("MainWindow", "*********"))
        self.pushButton_6.setText(_translate("MainWindow", "*********"))

    def mess(self):
        self.second_ui = SecondUI()
        self.second_ui.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
