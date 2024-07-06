import configparser
from PyQt6.QtWidgets import QMessageBox

SHORTCUT_CONFIG_FILE_NAME = 'shortcuts.conf'
SECTION_NAME = "Shortcuts"

def write_shortcut(character, shortcut):
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read(SHORTCUT_CONFIG_FILE_NAME, encoding='utf-8')
    
    if config.has_option(SECTION_NAME, shortcut):
        used_character = config[SECTION_NAME][shortcut]
        QMessageBox.information(None, "Shortcut Error", "The entered shortcut is already in use for " + used_character)
        return
    config[SECTION_NAME][shortcut] = character

    with open(SHORTCUT_CONFIG_FILE_NAME, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def get_character_from_shortcut(shortcut):
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read(SHORTCUT_CONFIG_FILE_NAME, encoding='utf-8')

    if config.has_option(SECTION_NAME, shortcut):
        return config.get(SECTION_NAME, shortcut)
    return None