from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QMessageBox, QLineEdit, QLabel, QScrollArea
from configservice import write_shortcut, write_special_character, get_special_character_list
from exceptions import (ShortcutInUseException,
                        ShortcutContainsStartCharException
)
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

        special_characters = get_special_character_list()
        symbol_binding_widget = SymbolBindingWidget()
        for char in special_characters:
            symbol_binding_widget.addSymbolBindingLine(char)

        self.scroll = QScrollArea()
        self.scroll.setWidget(symbol_binding_widget)
        self.addSymbolButton = self.createAddSymbolButton()
        self.applyButton = self.createApplyButton(symbol_binding_widget.saveShortcuts)

        grid.addWidget(self.scroll, 1, 1, 1, 2)
        grid.addWidget(self.applyButton, 2, 1)
        grid.addWidget(self.addSymbolButton, 2, 2)
        grid.setSpacing(5)
        self.setWindowTitle('Math Bindings')
    
    def createAddSymbolButton(self):
        button = QPushButton('Add new special characters')
        button.clicked.connect(lambda: self.createAddSpecialSymbolWindow())
        return button
    
    def createApplyButton(self, apply_function):
        button = QPushButton('Apply')
        button.clicked.connect(lambda: apply_function())
        return button

    def createAddSpecialSymbolWindow(self):
        label = 'Please entire the special symbols you want to add separated by commas:'
        window_title = 'Add Special Symbols'
        self.addSpecialSymbolWindow = GenericLineEntryBox(window_title, label, self.add_special_characters)
        self.addSpecialSymbolWindow.show()
    
    def add_special_characters(self, parent, code_list):
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
        
        symbol_binding_widget = self.scroll.widget()
        for char in unicode_chrs:
            write_special_character(char)
            symbol_binding_widget.addSymbolBindingLine(char)

        if failed_codes != []:
            message = 'Failed to add special characters for codes ' + ', '.join(failed_codes) + '. Please check that these codes are valid unicode characters.'
            QMessageBox.information(parent, 'Error', message)
            return False
        return True

    def convert_input_to_unicode_character(self, input):
        try:
            input_as_int = int(input, 16)
            unicode_chr = chr(input_as_int)
        except:
            return None
        return unicode_chr

class SymbolBindingWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initLogic()

    def initUI(self):
        self.grid = QGridLayout()
        self.setLayout(self.grid)

    def initLogic(self):
        self.symbolBindingLineList = []

    def addSymbolBindingLine(self, char):
        new_symbol_binding_line = SymbolBindingLine(char)
        self.symbolBindingLineList.append(new_symbol_binding_line)
        self.grid.addWidget(new_symbol_binding_line, self.grid.rowCount(), 1)

    def saveShortcuts(self):
        for line in self.symbolBindingLineList:
            line.save_shortcut()

class SymbolBindingLine(QWidget):

    def __init__(self, char):
        super().__init__()

        self.char = char
        self.changed = False
        self.initUI()
    
    def initUI(self):
        self.label = QLabel(self.char + ':', self)
        self.lineEntry = QLineEdit(self)
    
        self.lineEntry.textChanged.connect(lambda: self.set_changed(True))

        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(self.label, 1, 1)
        grid.addWidget(self.lineEntry, 1, 2)

    def get_char(self):
        return self.char
    
    def get_shortcut(self):
        return self.lineEntry.text()

    def set_changed(self, new_value):
        self.changed = new_value
    
    def save_shortcut(self):
        if self.changed:
            try:
                write_shortcut(self.char, self.lineEntry.text())
            except ShortcutInUseException as e:
                print('Shortcut in use')
            except ShortcutContainsStartCharException as e:
                print('Shortcut contains start character')
        return None