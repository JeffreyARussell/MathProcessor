from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextCursor, QKeySequence
from PyQt6.QtWidgets import QTextEdit
from configservice import get_character_from_shortcut

WHITESPACE_KEYS = [
    Qt.Key.Key_Tab.value,
    Qt.Key.Key_Return.value,
    Qt.Key.Key_Enter.value,
    Qt.Key.Key_Space.value
]
SHORTCUT_START_CHAR = '/'
SHORTCUT_START_KEY = QKeySequence.fromString(SHORTCUT_START_CHAR)[0].key().value
CODE_TERMINATER_KEYS = [
    *WHITESPACE_KEYS,
    SHORTCUT_START_KEY
]
MAX_SEARCH_DISTANCE = 4

class MainTextWindow(QTextEdit):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.initLogic()

    def initUI(self):
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
            break

        return super().keyPressEvent(e)
    
    def replaceShortcutWithCharacter(self, character):
        if character is None:
            return
        self.append(character)