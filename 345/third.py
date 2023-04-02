class CursorPositionError(Exception):
    pass


class LenError(Exception):
    pass


class CharacterError(Exception):
    pass


class FileError(Exception):
    pass


class Cursor:
    '''class for cursor'''

    def __init__(self, document):
        '''Construct'''
        self.document = document
        self.position = 0

    def forward(self):
        '''Forward'''
        try:
            if self.position == len(self.document.characters):
                raise CursorPositionError()
            self.position += 1
        except CursorPositionError:
            print("Cursor cannot move forward.")

    def back(self):
        '''back'''
        try:
            if self.position == 0:
                raise CursorPositionError()
            self.position -= 1
        except CursorPositionError:
            print("Cursor cannot move backward.")

    def home(self):
        '''home'''
        try:
            while self.document.characters[self.position-1].character != '\n':
                self.position -= 1
                if self.position == 0:
                    break
        except IndexError:
            print('Something is wrong with indexes')

    def end(self):
        '''end'''
        while self.position < len(self.document.characters) and self.document.characters[self.position] != '\n':
            self.position += 1


class Document:
    '''class Document'''

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        '''Insert'''
        if not hasattr(character, 'character'):
            try:
                character = str(character)

                if len(character) != 1:
                    raise LenError
            except LenError:
                print('You can add only one symbol')
            finally:
                character = Character(character[0])
                print(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        '''delete the character'''
        try:
            if self.cursor.position == 0:
                raise CursorPositionError
        except CursorPositionError:
            print("Cursor cannot delete backward.")
        del self.characters[self.cursor.position]

    def save(self):
        '''Save the elem'''
        try:
            f = open(self.filename, 'w')
            f.write(''.join(str(c) for c in self.characters))
            f.close()
        except:
            raise FileError("Unable to save file.")

    @property
    def string(self):
        '''Return'''
        return ''.join(str(c) for c in self.characters)


class Character:
    '''Character class'''

    def __init__(self, character, bold=False, italic=False, underline=False):
        '''Constructor'''
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        '''print the character'''
        bold = '*' if self.bold else ''
        italic = '/' if self.italic else ''
        underline = '_' if self.underline else ''
        return bold+italic+underline+self.character
