import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_value = 50
        self.init_value2 = 50
        self.slider = QSlider(Qt.Horizontal, self)
        self.label = QLabel(self)
        self.slider2 = QSlider(Qt.Horizontal, self)
        self.label2 = QLabel(self)
        self.oper = -1
        self.initUI()

    def initUI(self):
        r_botton = QFormLayout(self)
        self.slider_b(self.slider, self.label)
        self.slider_b(self.slider2, self.label2)
        r_botton.addRow(self.label, self.slider)
        r_botton.addRow(self.label2, self.slider2)

        botton = QHBoxLayout(self)
        botton.addStretch(1)

        add_b = QPushButton("Add")
        add_b.clicked.connect(self.click)
        botton.addWidget(add_b)
        self.add_b = add_b

        sub_b = QPushButton("Subtract")
        sub_b.clicked.connect(self.click)
        botton.addWidget(sub_b)
        self.sub_b = sub_b

        mul_b = QPushButton("Multiply")
        mul_b.clicked.connect(self.click)
        botton.addWidget(mul_b)
        self.mul_b = mul_b

        di_b = QPushButton("Divide")
        di_b.clicked.connect(self.click)
        botton.addWidget(di_b)
        self.di_b = di_b

        r_botton.addRow(botton)

        result = QLabel("Result")
        re_botton = QHBoxLayout(self)
        self.edit = QLineEdit()
        self.edit.setStyleSheet("background-color: gray ; color: yellow")
        self.edit.setFont(QFont("Arial", 10))
        self.edit.setAlignment(Qt.AlignRight)
        re_botton.addWidget(self.edit)
        r_botton.addRow(result, re_botton)

        self.adjustSize()
        self.setWindowTitle('Simple Calculator')
        self.show()

    def slider_b(self, slider, label):
        slider.setMinimum(0)
        slider.setMaximum(100)
        slider.setValue(50)
        slider.setTickPosition(self.slider.TicksBelow)
        slider.setTickInterval(5)
        slider.setGeometry(30, 40, 300, 50)
        slider.valueChanged[int].connect(self.change_value)

        label.setText(str(self.init_value))
        label.setFont(QFont("Arial", 20))
        label.setStyleSheet("color: blue")
        label.setGeometry(170, 20, 80, 30)

    def change_value(self, value):
        sender = self.sender()
        updated_value = value
        if sender == self.slider:
            self.label.setText(str(updated_value))
            self.updated_value = updated_value
            self.init_value = updated_value
        elif sender == self.slider2:
            self.label2.setText(str(updated_value))
            self.updated_value2 = updated_value
            self.init_value2 = updated_value
        self.cal()

    def click(self):
        sender = self.sender()
        self.cal()
        if sender.text() == "Add":
            b1 = "green"
            b2, b3, b4  = "white", "white", "white"
            self.oper = 0
        elif sender.text() == "Subtract":
            b2 = "green"
            b1, b3, b4 = "white", "white", "white"
            self.oper = 1
        elif sender.text() == "Multiply":
            b3 = "green"
            b1, b2, b4 = "white", "white", "white"
            self.oper = 2
        elif sender.text() == "Divide":
            b4 = "green"
            b1, b2, b3 = "white", "white", "white"
            self.oper = 3
        self.add_b.setStyleSheet(f"background-color: {b1} ")
        self.sub_b.setStyleSheet(f"background-color: {b2}")
        self.mul_b.setStyleSheet(f"background-color: {b3}")
        self.di_b.setStyleSheet(f"background-color: {b4}")

    def cal(self):
        num1 = self.init_value
        num2 = self.init_value2
        if self.oper == 0:
            ans = num1 + num2
            self.edit.setText(str(ans))
        elif self.oper == 1:
            ans = num1 - num2
            self.edit.setText(str(ans))
        elif self.oper == 2:
            ans = num1 * num2
            self.edit.setText(str(ans))
        elif self.oper == 3:
            if num2 == 0:
                self.edit.setText("Can't devide by zero")
            else:
                ans = num1 / num2
                self.edit.setText(str(ans))
        else:
            pass


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()