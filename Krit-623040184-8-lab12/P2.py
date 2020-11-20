import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.label = QLabel(self)
        self.edit = QTextEdit()
        self.fbox = QFormLayout()
        self.init_ui()
        self.bg_color = ""
        self.font_color = ""
        self.file_path = ""

    def init_ui(self):
        menu = self.menuBar()
        file_menu = menu.addMenu('File')
        edit_menu = QMenu('Edit', self)

        color_menu = QMenu("Color", self)
        edit_menu.addMenu(color_menu)

        background_act = QAction("Background color", self)
        background_act.triggered.connect(self.background_update)
        foreground_act = QAction("Foreground color", self)
        foreground_act.triggered.connect(self.foreground_update)
        menu.addMenu(edit_menu)
        color_menu.addAction(background_act)
        color_menu.addAction(foreground_act)

        font_act = QAction("Font", self)
        edit_menu.addAction(font_act)

        open_act = QAction('open', self)
        open_act.setShortcut("Ctrl+O")
        open_act.triggered.connect(self.opening)
        file_menu.addAction(open_act)

        save_act = QAction('save', self)
        save_act.setShortcut("Ctrl+S")
        save_act.triggered.connect(self.saving)
        file_menu.addAction(save_act)

        self.edit.setFont(QFont("Arial", 16))
        self.setCentralWidget(self.edit)

        self.setLayout(self.fbox)
        self.setGeometry(500, 300, 300, 200)
        self.setWindowTitle("File dialog")
        self.show()

    def saving(self):
        if not self.file_path:
            new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Save this file as...", "untitled.txt", "Text files (.txt)")
            if new_file_path:
                self.file_path = new_file_path
            else:
                self.invalid_path_alert_message()
            return False

        with open(self.file_path, "w") as file:
            file.write(self.edit.toPlainText())

    def opening(self):
        name = QFileDialog.getOpenFileName()
        with open(name[0]) as file:
            self.edit.setText(file.read())

    def background_update(self):
        self.bg_color = QColorDialog.getColor()
        try:
            self.edit.setStyleSheet(f"background-color: {self.bg_color.name()}; color: {self.font_color.name()}" )
        except:
            self.edit.setStyleSheet(f"background-color: {self.bg_color.name()}")

    def foreground_update(self):
        self.font_color = QColorDialog.getColor()
        try:
            self.edit.setStyleSheet(f"background-color: {self.bg_color.name()}; color: {self.font_color.name()}")
        except:
            self.edit.setStyleSheet(f"background-color: {self.font_color.name()}")


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()