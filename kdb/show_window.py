from PyQt5.QtWidgets import QMainWindow, QApplication
from window_main import Ui_MainWindow  # 导入主窗体文件中的ui类
import sys
# 出窗体初始化类
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 主窗体对象
    main = Main()
    # 显示主窗体
    main.show()



    sys.exit(app.exec_())
