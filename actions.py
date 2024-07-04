from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QAction

def getExitAct(parentWidget):
    exitAct = QAction('&Exit', parentWidget)
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    exitAct.triggered.connect(QApplication.instance().quit)
    return exitAct

def getSaveAct(parentWidget):
    saveAct = QAction('&Save', parentWidget)
    saveAct.setShortcut('Ctrl+S')
    saveAct.setStatusTip('Save document')
    return saveAct

def getOpenAct(parentWidget):
    openAct = QAction('&Open', parentWidget)
    openAct.setShortcut('Ctrl+O')
    openAct.setStatusTip('Open document')
    return openAct