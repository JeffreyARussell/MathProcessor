from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QLineEdit
from actions import getExitAct
from configservice import write_shortcut, write_special_character, get_special_character_list
from genericlineentrybox import GenericLineEntryBox

class SettingsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 350, 200)

class MathBindingsWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        mathChars = get_special_character_list() # ['\u222B', '\u2200', '\u2203', '\u2204', '\u2205', '\u2208', '\u2210']

        HORIZONTAL = 5
        vertical = len(mathChars) // 5 + 1
        positions = [(i, j) for i in range(vertical) for j in range(HORIZONTAL)]

        for position, name in zip(positions, mathChars):
            grid.addWidget(self.createMathSymbolEntry(name), *position)
        
        self.addSymbolButton = self.createAddSymbolButton()
        grid.addWidget(self.addSymbolButton, vertical, 2)
        self.setWindowTitle('Math Bindings')

    def reload_grid(self):
        grid = self.layout()
        grid.removeWidget(self.addSymbolButton)
        mathChars = get_special_character_list() # ['\u222B', '\u2200', '\u2203', '\u2204', '\u2205', '\u2208', '\u2210']

        HORIZONTAL = 5
        vertical = len(mathChars) // 5 + 1
        positions = [(i, j) for i in range(vertical) for j in range(HORIZONTAL)]

        for position, name in zip(positions, mathChars):
            grid.addWidget(self.createMathSymbolEntry(name), *position)
        
        grid.addWidget(self.addSymbolButton, vertical, 2)

    def createMathSymbolEntry(self, name):
        button = QPushButton(name)
        button.clicked.connect(lambda: self.createMathSymbolShortcutWindow(name))
        return button
    
    def createAddSymbolButton(self):
        button = QPushButton('Add new special characters')
        button.clicked.connect(lambda: self.createAddSpecialSymbolWindow())
        return button
    
    def createMathSymbolShortcutWindow(self, name):
        label = 'Please enter the code for the ' + name + ' symbol.'
        window_title = name + " Code"
        self.mathSymbolWindow = GenericLineEntryBox(window_title, label, write_shortcut, [name])
        self.mathSymbolWindow.show()

    def createAddSpecialSymbolWindow(self):
        label = 'Please entire the special symbols you want to add separated by commas:'
        window_title = 'Add Special Symbols'
        self.addSpecialSymbolWindow = GenericLineEntryBox(window_title, label, self.write_special_character_and_refresh, [])
        self.addSpecialSymbolWindow.show()

    def write_special_character_and_refresh(self, name):
        write_special_character(name)
        self.reload_grid()