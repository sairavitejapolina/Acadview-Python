import sys
import os
from PyQt5.QtWidgets import QApplication, QTextEdit, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog,QAction, qApp, QMainWindow, QFontDialog


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QTextEdit(self)
        self.clr_btn = QPushButton('Clear')
        self.save_btn = QPushButton('Save')
        self.open_btn = QPushButton('Open')

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.clr_btn)
        h_layout.addWidget(self.open_btn)

        v_layout.addWidget(self.text)
        v_layout.addWidget(self.clr_btn)
        v_layout.addWidget(self.save_btn)
        v_layout.addWidget(self.open_btn)
        self.clr_btn.clicked.connect(self.clear_text)
        self.save_btn.clicked.connect(self.save_text)
        self.open_btn.clicked.connect(self.open_text)
        self.setLayout(v_layout)
        self.setWindowTitle('My Text Editor in PEP')
        self.show()

    def clear_text(self):
        self.text.clear()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save your file', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self,'Open your file',os.getenv('HOME'))
        with open(filename[0],'r') as f:
            file_text=f.read()
            self.text.setText(file_text)

class Writer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)
        self.init_ui()
    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')
        edit = bar.addMenu('Edit')
        new = QAction('New File',self)
        new.setShortcut('Ctrl+N')
        save = QAction('Save File',self)
        save.setShortcut('Ctrl+S')
        open = QAction('Open File',self)
        open.setShortcut('Ctrl+O')
        quitt = QAction('Quit',self)
        quitt.setShortcut('Ctrl+W')
        file.addAction(new)
        file.addAction(save)
        file.addAction(open)
        file.addAction(quitt)

        font = QAction('Font Settings',self)
        font.setShortcut('Ctrl+E')
        edit.addAction(font)
        quitt.triggered.connect(self.quit_trigger)
        file.triggered.connect(self.respond)
        edit.triggered.connect(self.editfont)
        self.show()
    def respond(self,q):
        signal = q.text()
        if signal == 'New File':
            self.form_widget.clear_text()

        elif signal == 'Open File':
            self.form_widget.open_text()
        elif signal == 'Save File':
            self.form_widget.save_text()

    def editfont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.TextEdit.setFont(font)

    def clear_text(self):
        self.text.clear()

    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save your file', os.getenv('HOME'))
        with open(filename[0], 'w') as f:
            my_text = self.text.toPlainText()
            f.write(my_text)

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self,'Open your file',os.getenv('HOME'))
        with open(filename[0],'r') as f:
            file_text=f.read()
            self.text.setText(file_text)



    def quit_trigger(self):
        qApp.quit()


app = QApplication(sys.argv)
writer = Writer()
sys.exit(app.exec_())
