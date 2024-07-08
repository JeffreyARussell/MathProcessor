import os
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QKeySequence

#Config constants
SHORTCUT_CONFIG_FILE_NAME = 'shortcuts.conf'
SHORTCUT_SECTION_NAME = "Shortcuts"
SPECIAL_CHARACTERS_SECTION_NAME = "Special_Characters"
SPECIAL_CHARACTERS_OPTION_NAME = 'special_characters_list'
SECTION_NAMES = [
    SHORTCUT_SECTION_NAME,
    SPECIAL_CHARACTERS_SECTION_NAME
]
CONFIG_PATH = os.path.join(os.getcwd(), SHORTCUT_CONFIG_FILE_NAME)

#Shortcut replacement constants
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
    Qt.Key.Key_Slash.value
]
CODE_COMPLETION_KEY = Qt.Key.Key_Tab.value
MAX_SEARCH_DISTANCE = 4