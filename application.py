#!/usr/bin/python

import sys
import os
from mainmenu import MainMenuBar
from actions import getExitAct
from maintoolbar import MainToolBar
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QApplication, QTextEdit, QInputDialog
from PyQt6.QtGui import QTextDocument

MAGIC_SIZE_LIMIT = 10000

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initLogic()

    def initLogic(self):
        self.currentDocPath = None

    def initUI(self):
        self.setGeometry(300, 300, 350, 200)
        self.center()
        self.setWindowTitle('New Document')
        self.initMenuBar()

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        self.show()

    def initMenuBar(self):
        self.setMenuBar(MainMenuBar(self, saveFunction=self.saveText, openFunction=self.openFile))

        self.toolbar = self.addToolBar(MainToolBar(self))

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                    "Are you sure you want to quit?", QMessageBox.StandardButton.Yes |
                    QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()

    def saveText(self):
        if self.currentDocPath is None:
            title, ok = QInputDialog.getText(self, 'Save', 'Please enter a name for the document.')
            if not ok:
                QMessageBox.information(title='Error', test="This failed but I don't know why!")
            self.currentDocPath = os.path.join(os.getcwd(), title)

        f = open(self.currentDocPath, 'w')
        f.write(self.centralWidget().toPlainText())
        f.close()

    def openFile(self):
        title, ok = QInputDialog.getText(self, 'Save', 'Please enter the name of the document.')
        if not ok:
            QMessageBox.information(self, 'Error', "This failed but I don't know why!")
        path = os.path.join(os.getcwd(), title)

        try:
            f = open(path, 'r')
        except FileNotFoundError:
            QMessageBox.information(self, 'Read Error', 'Read failed, please check that the file exists.')
            return
        
        with f:
            doc = QTextDocument(f.read(MAGIC_SIZE_LIMIT), parent=self.centralWidget())
        
        self.centralWidget().setDocument(doc)

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()