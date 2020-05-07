import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using LineEdits")
        self.setGeometry(50, 50, 350, 350)

        self.nameTextBox = QLineEdit(self)
        self.passTextBox = QLineEdit(self)

        self.ui()

    def ui(self):
        self.nameTextBox.setPlaceholderText("Please Enter your Name!")
        self.nameTextBox.move(120, 50)
        self.passTextBox.setPlaceholderText("Please Enter your Password!")
        self.passTextBox.setEchoMode(QLineEdit.Password)
        self.passTextBox.move(120, 80)
        button = QPushButton("Save", self)
        button.move(180, 110)
        button.clicked.connect(self.get_values)
        self.show()

    def get_values(self):
        name = self.nameTextBox.text()
        password = self.passTextBox.text()
        self.setWindowTitle(f"Your Name is {name} Your Password is : {password}")


def main():
    app = QApplication(sys.argv)
    windows = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
