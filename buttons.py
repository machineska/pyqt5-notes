import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 350, 350)
        self.text = QLabel("My Text", self)
        self.ui()

    def ui(self):
        enter_button = QPushButton("Enter", self)
        exit_button = QPushButton("Exit", self)
        self.text.move(160, 50)
        enter_button.move(100, 80)
        exit_button.move(200, 80)
        enter_button.clicked.connect(self.enter_func)
        exit_button.clicked.connect(self.exit_func)
        self.show()

    def enter_func(self):
        self.text.setText("You clicked Enter")
        self.text.resize(150, 20)

    def exit_func(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150, 20)


def main():
    app = QApplication(sys.argv)
    windows = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
