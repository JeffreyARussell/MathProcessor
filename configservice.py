import configparser
import os
from PyQt6.QtWidgets import QMessageBox
from constants import (CONFIG_PATH,
                    SECTION_NAMES,
                    SHORTCUT_CONFIG_FILE_NAME,
                    SHORTCUT_SECTION_NAME,
                    SPECIAL_CHARACTERS_OPTION_NAME,
                    SPECIAL_CHARACTERS_SECTION_NAME
                    )

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

    with open(SHORTCUT_CONFIG_FILE_NAME, 'w') as f:
        config.write(f)

def write_shortcut(character, shortcut):
    config = get_config_parser()
    
    if config.has_option(SHORTCUT_SECTION_NAME, shortcut):
        used_character = config[SHORTCUT_SECTION_NAME][shortcut]
        QMessageBox.information(None, "Shortcut Error", "The entered shortcut is already in use for " + used_character)
        return
    config[SHORTCUT_SECTION_NAME][shortcut] = character

    with open(SHORTCUT_CONFIG_FILE_NAME, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def get_character_from_shortcut(shortcut):
    config = get_config_parser()

    return config.get(SHORTCUT_SECTION_NAME, shortcut, fallback=None)

def write_special_character(character):
    print(character)
    config = get_config_parser()

    special_characters = config.get(SPECIAL_CHARACTERS_SECTION_NAME, SPECIAL_CHARACTERS_OPTION_NAME, fallback=None)
    if special_characters == None:
        new_list = character
    elif character in special_characters.split(','):
        return
    else:
        new_list = special_characters + ',' + character
    print(new_list)

    config[SPECIAL_CHARACTERS_SECTION_NAME][SPECIAL_CHARACTERS_OPTION_NAME] = new_list

    with open(SHORTCUT_CONFIG_FILE_NAME, 'w', encoding='utf-8') as configfile:
        config.write(configfile)

def get_special_character_list():
    config = get_config_parser()

    special_characters = config.get(SPECIAL_CHARACTERS_SECTION_NAME, SPECIAL_CHARACTERS_OPTION_NAME, fallback=None)
    if special_characters == None:
        return []
    return special_characters.split(',')

def get_config_parser():
    config = configparser.ConfigParser()
    config.optionxform = lambda option: option
    config.read(SHORTCUT_CONFIG_FILE_NAME, encoding='utf-8')
    return config