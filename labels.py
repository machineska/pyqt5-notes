import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.ui()

    def ui(self):
        text1 = QLabel("Hello Python", self)
        text2 = QLabel("Hello World", self)
        text1.move(100, 50)
        text2.move(200, 50)
        self.show()


def main():
    app = QApplication(sys.argv)
    windows = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
