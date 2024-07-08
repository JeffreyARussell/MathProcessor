from PyQt6.QtGui import QTextCursor, QFont
from PyQt6.QtWidgets import QTextEdit
from configservice import get_character_from_shortcut
from constants import (CODE_COMPLETION_KEY,
                       CODE_TERMINATER_KEYS,
                       MAX_SEARCH_DISTANCE,
                       SHORTCUT_START_CHAR)

class MainTextWindow(QTextEdit):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initLogic()

    def initUI(self):
        math_font = QFont('Cambria Math', pointSize=15)
        self.setFont(math_font)
        return
    
    def initLogic(self):
        self.trackingCode = False
        self.currentCode = []

    def resetLogic(self):
        self.trackingCode = False
        self.currentCode = []
    
    def keyPressEvent(self, e) -> None:
        cursor = self.textCursor()
        if e.key() not in CODE_TERMINATER_KEYS:
            return super().keyPressEvent(e)
        for i in range(MAX_SEARCH_DISTANCE):
            cursor.movePosition(QTextCursor.MoveOperation.Left, QTextCursor.MoveMode.KeepAnchor)
            selection = cursor.selectedText()
            if not selection.startswith(SHORTCUT_START_CHAR):
                continue

            selection = selection[1:]
            character = get_character_from_shortcut(selection)
            if not character is None:
                cursor.insertText(character)
                if e.key() == CODE_COMPLETION_KEY:
                    return
            break

        return super().keyPressEvent(e)
    
    def replaceShortcutWithCharacter(self, character):
        if character is None:
            return
        self.append(character)