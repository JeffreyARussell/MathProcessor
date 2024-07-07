from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox
from configservice import write_shortcut, write_special_character, get_special_character_list, get_shortcut_from_character
from constants import SHORTCUT_START_CHAR
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
        current_shortcut = get_shortcut_from_character(name)
        self.mathSymbolWindow = GenericLineEntryBox(window_title, label, self.validate_and_write_math_shortcut, save_function_options=[name], default_text=current_shortcut)
        self.mathSymbolWindow.show()

    def createAddSpecialSymbolWindow(self):
        label = 'Please entire the special symbols you want to add separated by commas:'
        window_title = 'Add Special Symbols'
        self.addSpecialSymbolWindow = GenericLineEntryBox(window_title, label, self.write_special_character_and_refresh)
        self.addSpecialSymbolWindow.show()

    def validate_and_write_math_shortcut(self, parent, name, shortcut):
        if shortcut.find(SHORTCUT_START_CHAR) != -1:
            QMessageBox.information(parent, 'Error', 'You cannot use the shortcut start character in a shortcut, please try again.')
            return False
        write_shortcut(name, shortcut)
        return True
                

    def write_special_character_and_refresh(self, parent, code_list):
        if code_list == "":
                return
            
        codes = code_list.split(',')
        unicode_chrs = []
        failed_codes = []
        for code in codes:
            result = self.convert_input_to_unicode_character(code)
            if result is None:
                failed_codes.append(code)
            else:
                unicode_chrs.append(result)
        if unicode_chrs == []:
            QMessageBox.information(parent, 'Error', 'All special characters failed to add. Please check that your code is a valid unicode character.')
            return False
        elif failed_codes != []:
            message = 'Failed to add special characters for codes ' + ', '.join(failed_codes) + '. Please check that these codes are valid unicode characters.'
            QMessageBox.information(parent, 'Error', message)
            return False
        
        for char in unicode_chrs:
            write_special_character(char)
        self.reload_grid()
        return True

    def convert_input_to_unicode_character(self, input):
        try:
            input_as_int = int(input, 16)
            unicode_chr = chr(input_as_int)
        except:
            return None
        return unicode_chr