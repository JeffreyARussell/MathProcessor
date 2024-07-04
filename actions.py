from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QAction
from settings import SettingsWindow, MathBindingsWindow

def getExitAct(parentWidget):
    exitAct = QAction('&Exit', parentWidget)
    exitAct.setShortcut('Ctrl+Q')
    exitAct.setStatusTip('Exit application')
    exitAct.triggered.connect(QApplication.instance().quit)
    return exitAct

def getSettingsAct(parentWidget):
    settingsAct = QAction('&Settings', parentWidget)
    settingsAct.setShortcut("Ctrl+I")
    settingsAct.setStatusTip('Open settings')
    settingsAct.triggered.connect(lambda: createSettingsWindowEvent(parentWidget))
    return settingsAct

def getMathBindingsAct(parentWidget):
    mathBindingsAct = QAction('&Math Bindings', parentWidget)
    mathBindingsAct.setShortcut("Ctrl+M")
    mathBindingsAct.setStatusTip('Open the list of bindings for math characters.')
    mathBindingsAct.triggered.connect(lambda: createMathBindingsEvent(parentWidget))
    return mathBindingsAct

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

def createSettingsWindowEvent(parentWidget):
    if not hasattr(parentWidget, "settings"):
        parentWidget.settings = SettingsWindow()
        parentWidget.settings.show()
    else:
        parentWidget.settings.show()

def createMathBindingsEvent(parentWidget):
    if not hasattr(parentWidget, "mathbindings"):
        parentWidget.mathbindings = MathBindingsWindow()
        parentWidget.mathbindings.show()
    else:
        parentWidget.mathbindings.show()