import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class CheckDemo(QWidget):
    def __init__(self, parent=None):
        super(CheckDemo, self).__init__(parent)

        layout = QHBoxLayout()
        label_name = QLabel("Name")
        self.edit_name = QLineEdit()
        layout.addWidget(label_name)
        layout.addWidget(self.edit_name)
        fbox = QFormLayout(self)
        fbox.addRow(label_name, self.edit_name)

        layout = QHBoxLayout(self)
        self.b1 = QCheckBox("PyQt")
        self.b1.setChecked(True)
        self.b1.stateChanged.connect(lambda: self.chk_state(self.b1))
        layout.addWidget(self.b1)

        self.b2 = QCheckBox("PyGame")
        self.b2.toggled.connect(lambda: self.chk_state(self.b2))
        layout.addWidget(self.b2)

        self.b3 = QCheckBox("PyTorch")
        self.b3.toggled.connect(lambda: self.chk_state(self.b3))
        layout.addWidget(self.b3)

        layout.addStretch()
        fbox.addRow(QLabel("Libery"), layout)

        layout.addStretch(1)
        self.summit = QPushButton("Summit")
        self.summit.clicked.connect(self.text)
        cancel = QPushButton("Cancel")

        layout.addWidget(self.summit)
        layout.addWidget(cancel)

        self.setLayout(layout)
        self.setGeometry(300, 300, 350, 150)
        self.setWindowTitle('Problem 3')
        self.show()

    def text(self):
        ui_text = self.edit_name.text()
        if ui_text == "":
            pass
        else:
            print(f"Name is {ui_text}")

    def chk_state(self, b):
        if b.isChecked() == True:
            print(b.text()+"is selected")
        else:
            print(b.text()+"is deselected")

def main():
    app = QApplication(sys.argv)
    ex = CheckDemo()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()