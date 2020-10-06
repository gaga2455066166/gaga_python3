import sys
import pcc
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("MainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget.setGeometry(QtCore.QRect(280, 50, 451, 502))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.pushButton.setMinimumSize(QtCore.QSize(50, 500))
        self.pushButton.setStyleSheet("border-image: url(:/newPrefix/1.jpg);")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        # self.pushButton.clicked.connect(self.hello)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.pushButton.clicked.connect(self.hello)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "大帅比"))

    @staticmethod
    def hello():
        print("hello world")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
