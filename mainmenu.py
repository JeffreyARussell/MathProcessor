from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction
from actions import getExitAct, getSaveAct, getOpenAct
from settings import SettingsWindow, MathBindingsWindow

class MainMenuBar(QMenuBar):
    def __init__(self, parent, saveFunction, openFunction):
        super().__init__(parent)

        self.initMenu(saveFunction, openFunction)
    
    def initMenu(self,  saveFunction, openFunction):
        exitAct = getExitAct(self)

        settingsAct = self.getSettingsAct()

        saveAct = getSaveAct(self)
        saveAct.triggered.connect(saveFunction)

        openAct = getOpenAct(self)
        openAct.triggered.connect(openFunction)

        mathBindingsAct = self.getMathBindingsAct()

        fileMenu = self.addMenu('&File')
        fileMenu.addAction(saveAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(exitAct)

        settingsMenu = self.addMenu('&Settings')
        settingsMenu.addAction(mathBindingsAct)
        settingsMenu.addAction(settingsAct)

    def getSettingsAct(self):
        settingsAct = QAction('&Settings', self)
        settingsAct.setShortcut("Ctrl+I")
        settingsAct.setStatusTip('Open settings')
        settingsAct.triggered.connect(lambda: self.createSettingsWindowEvent())
        return settingsAct

    def getMathBindingsAct(self):
        mathBindingsAct = QAction('&Math Bindings', self)
        mathBindingsAct.setShortcut("Ctrl+M")
        mathBindingsAct.setStatusTip('Open the list of bindings for math characters.')
        mathBindingsAct.triggered.connect(lambda: self.createMathBindingsEvent())
        return mathBindingsAct

    def createSettingsWindowEvent(self, parentWidget):
        if not hasattr(parentWidget, "settings"):
            self.settings = SettingsWindow()
            self.settings.show()
        else:
            self.settings.show()

    def createMathBindingsEvent(self):
        if not hasattr(self, "mathbindings"):
            self.mathbindings = MathBindingsWindow()
            self.mathbindings.show()
        else:
            self.mathbindings.show()