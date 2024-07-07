class ShortcutContainsStartCharException(Exception):

    def __init__(self):
        super().__init__()

class ShortcutInUseException(Exception):
    
    def __init__(self, char_in_use_for):
        super().__init__()
        self.char = char_in_use_for

    def get_char(self):
        return self.char