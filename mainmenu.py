from PyQt6.QtWidgets import QMenuBar
from actions import getExitAct, getSettingsAct, getSaveAct, getOpenAct, getMathBindingsAct

class MainMenuBar(QMenuBar):
    def __init__(self, parent, saveFunction, openFunction):
        super().__init__(parent)

        self.initMenu(saveFunction, openFunction)
    
    def initMenu(self,  saveFunction, openFunction):
        exitAct = getExitAct(self)

        settingsAct = getSettingsAct(self)

        saveAct = getSaveAct(self)
        saveAct.triggered.connect(saveFunction)

        openAct = getOpenAct(self)
        openAct.triggered.connect(openFunction)

        mathBindingsAct = getMathBindingsAct(self)

        fileMenu = self.addMenu('&File')
        fileMenu.addAction(saveAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(exitAct)

        settingsMenu = self.addMenu('&Settings')
        settingsMenu.addAction(mathBindingsAct)
        settingsMenu.addAction(settingsAct)
