import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")

        new_act = QAction("New", self)

        file_menu.addAction(new_act)

        imp_menu = QMenu("Edit", self)
        imp_act1 = QAction("Copy", self)
        imp_act2 = QAction("Paste", self)

        file_menu.addMenu(imp_menu)
        imp_menu.addAction(imp_act1)
        imp_menu.addAction(imp_act2)

        save_act = QAction("Save", self)
        save_act.setShortcut("Crit+S")

        exit_act = QAction(QIcon("6YToyEF.png"), "Quit", self)
        exit_act.setShortcut("Crit+Q")
        exit_act.setStatusTip("Exit application")
        exit_act.triggered.connect(QApplication.instance().quit)

        file_menu.addAction(save_act)
        file_menu.addAction(exit_act)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Exercise 2")
        self.statusBar().showMessage("By Manee")
        self.statusBar().addPermanentWidget(QLabel("By Manee"), 1)
        self.show()


def main():
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()