from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox
import binascii
from configservice import write_shortcut

class GenericLineEntryBox(QWidget):

        def __init__(self, window_title, label_string, save_function, save_function_options):
            super().__init__()
            self.window_title = window_title
            self.label_string = label_string
            self.save_function = save_function
            self.save_function_options = save_function_options

            self.initUI()
        
        def initUI(self):
            shortcutLabel = QLabel(self.label_string, self)
            shortcutEdit = QLineEdit(self)

            button = QPushButton('Save')
            button.clicked.connect(lambda: self.saveButtonOnClick(shortcutEdit))

            grid = QGridLayout()
            grid.setSpacing(10)

            grid.addWidget(shortcutLabel, 1, 0)
            grid.addWidget(shortcutEdit, 1, 1)
            grid.addWidget(button, 2, 1)

            self.setLayout(grid)
            self.setWindowTitle(self.window_title)

        def saveButtonOnClick(self, shortcutLineEdit):
            if shortcutLineEdit.text() == "":
                return
            
            codes = shortcutLineEdit.text().split(',')
            unicode_chrs = []
            failed_codes = []
            for code in codes:
                result = self.convert_input_to_unicode_character(code)
                if result is None:
                    failed_codes.append(code)
                else:
                    unicode_chrs.append(result)
            if unicode_chrs == []:
                QMessageBox.information(self, 'Error', 'All special characters failed to add. Please check that your code is a valid unicode character.')
            elif failed_codes != []:
                message = 'Failed to add special characters for codes ' + ', '.join(failed_codes) + '. Please check that these codes are valid unicode characters.'
                QMessageBox.information(self, 'Error', message)
            
            for char in unicode_chrs:
                self.save_function(*self.save_function_options, char)
            self.destroy()

        def convert_input_to_unicode_character(self, input):
            try:
                input_as_int = int(input, 16)
                unicode_chr = chr(input_as_int)
            except:
                return None
            return unicode_chr
             