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
            entryLavel = QLabel(self.label_string, self)
            entryLineEdit = QLineEdit(self)

            button = QPushButton('Save')
            button.clicked.connect(lambda: self.saveButtonOnClick(entryLineEdit))

            grid = QGridLayout()
            grid.setSpacing(10)

            grid.addWidget(entryLavel, 1, 0)
            grid.addWidget(entryLineEdit, 1, 1)
            grid.addWidget(button, 2, 1)

            self.setLayout(grid)
            self.setWindowTitle(self.window_title)

        def saveButtonOnClick(self, entryLineEdit):
            if self.save_function_options == []:
                 self.save_function(entryLineEdit.text())
            else:
                 self.save_function(*self.save_function_options, entryLineEdit.text())
            self.destroy()
             