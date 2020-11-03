import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        btn = QPushButton("Quit", self)
        label = QLabel("My name is Manee", self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.setToolTip("kick to exit")
        btn.resize(btn.sizeHint())
        btn.move(115, 80)
        label.move(110, 60)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Quit button with tooltips")
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message",
                                     "Ae you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()