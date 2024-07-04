from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QLineEdit

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

        mathChars = ['\u222B', '\u2200', '\u2203', '\u2204', '\u2205', '\u2208']

        HORIZONTAL = 5
        vertical = len(mathChars) // 5 + 1
        positions = [(i, j) for i in range(vertical) for j in range(HORIZONTAL)]

        for position, name in zip(positions, mathChars):
            grid.addWidget(self.createMathSymbolEntry(name), *position)

        grid.addWidget(self.createSaveButton(), vertical, 1)
        grid.addWidget(self.createCancelButton(), vertical, 3)
        
        self.setWindowTitle('Math Bindings')

    def createMathSymbolEntry(self, name):
        button = QPushButton(name)
        button.clicked.connect(lambda: self.createMathSymbolShortcutWindow(name))
        return button
    
    def createMathSymbolShortcutWindow(self, name):
        self.mathSymbolWindow = MathBindingShortcutWindow(name)
        self.mathSymbolWindow.show()
    
    def createSaveButton(self):
        button = QPushButton('Save')
        return button
    
    def createCancelButton(self):
        button = QPushButton('Cancel')
        return button
    
class MathBindingShortcutWindow(QWidget):

        def __init__(self, math_char_name):
            super().__init__()

            self.math_char_name = math_char_name
            self.initUI()
        
        def initUI(self):
            shortcutLabel = QLabel('Please enter the code for the ' + self.math_char_name + ' symbol.', self)
            shortcutEdit = QLineEdit(self)

            grid = QGridLayout()
            grid.setSpacing(10)

            grid.addWidget(shortcutLabel, 1, 0)
            grid.addWidget(shortcutEdit, 1, 1)

            self.setLayout(grid)
            self.setWindowTitle(self.math_char_name + ' Shortcut')
