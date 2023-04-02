class VigenereCipher:
    '''class vignere'''
    def __init__(self, keyword):
        '''construct'''
        self.keyword = keyword

    def _code(self, text, combine_func):
        '''coding method'''
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for p, k in zip(text, keyword):
            combined.append(combine_func(p, k))
        return "".join(combined)

    def extend_keyword(self, number):
        '''extend keyword'''
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def separate_character(cypher, keyword):
        '''separate character'''
        cypher = cypher.upper()
        keyword = keyword.upper()
        cypher_num = ord(cypher) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (cypher_num - keyword_num) % 26)

    def combine_character(plain, keyword):
        '''combine character'''
        plain = plain.upper()
        keyword = keyword.upper()
        plain_num = ord(plain) - ord('A')
        keyword_num = ord(keyword) - ord('A')
        return chr(ord('A') + (plain_num + keyword_num) % 26)

    def encode(self, plaintext):
        '''encoding'''
        return self._code(plaintext, VigenereCipher.combine_character)

    def decode(self, ciphertext):
        '''decoding'''
        return self._code(ciphertext, VigenereCipher.separate_character)


