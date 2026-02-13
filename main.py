import sys
from PyQt5.QtWidgets import QApplication, QWidget
from qtui import Ui_Form  # 导入UI类

class FluentMain(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 初始化UI

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = FluentMain()
    window.show()
    sys.exit(app.exec_())
