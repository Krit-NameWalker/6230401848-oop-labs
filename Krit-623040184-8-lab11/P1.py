import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Problem 1')

        simple_label = QLabel("Simple Form", self)
        simple_label.setFont(QFont("Arial", 18))
        simple_label.setStyleSheet("color: blue")
        simple_label.adjustSize()

        label_name = QLabel("Name")
        edit_name = QLineEdit(self)

        fbox = QFormLayout(self)
        fbox.addRow(simple_label, simple_label)
        fbox.addRow(label_name, edit_name)
        vbox = QVBoxLayout(self)

        hbox = QHBoxLayout(self)
        radio_male = QRadioButton("Male")
        radio_female = QRadioButton("Female")
        hbox.addWidget(radio_male)
        hbox.addWidget(radio_female)
        hbox.addStretch()
        fbox.addRow(QLabel("Gender"), hbox)

        hbox = QHBoxLayout(self)
        hbox.addStretch(1)
        hbox.addWidget(QPushButton("Summit"))
        hbox.addWidget(QPushButton("Cancel"))
        fbox.addRow(hbox)

        self.show()


def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()