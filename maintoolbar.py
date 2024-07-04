from PyQt6.QtWidgets import QToolBar
from actions import getExitAct

class MainToolBar(QToolBar):
    def __init__(self, parentWidget):
        super().__init__(parentWidget)

        self.initToolBar()
    
    def initToolBar(self):
        self.addAction(getExitAct(self))