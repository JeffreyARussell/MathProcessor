import configparser
import os
from PyQt6.QtWidgets import QMessageBox

SHORTCUT_CONFIG_FILE_NAME = 'shortcuts.conf'
SHORTCUT_SECTION_NAME = "Shortcuts"
SECTION_NAMES = [
    SHORTCUT_SECTION_NAME
]
CONFIG_PATH = os.path.join(os.getcwd(), SHORTCUT_CONFIG_FILE_NAME)

def validate_config():
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    if not os.path.isfile(CONFIG_PATH):
        initialize_config_file(config)
        return

    config.read(SHORTCUT_CONFIG_FILE_NAME, encoding='utf-8')
    for section in SECTION_NAMES:
        if not config.has_section(section):
            initialize_section(section, config)

def initialize_config_file(config):
    for section in SECTION_NAMES:
        config[section] = {}

    with open(SHORTCUT_CONFIG_FILE_NAME, 'w') as f:
        config.write(f)

def initialize_section(section_name, config):
    config[section_name] = {}


def write_shortcut(character, shortcut):
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read(SHORTCUT_CONFIG_FILE_NAME, encoding='utf-8')
    
    if config.has_option(SHORTCUT_SECTION_NAME, shortcut):
        used_character = config[SHORTCUT_SECTION_NAME][shortcut]
        QMessageBox.information(None, "Shortcut Error", "The entered shortcut is already in use for " + used_character)
        return
    config[SHORTCUT_SECTION_NAME][shortcut] = character

    with open(SHORTCUT_CONFIG_FILE_NAME, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def get_character_from_shortcut(shortcut):
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read(SHORTCUT_CONFIG_FILE_NAME, encoding='utf-8')

    if config.has_option(SHORTCUT_SECTION_NAME, shortcut):
        return config.get(SHORTCUT_SECTION_NAME, shortcut)
    return None