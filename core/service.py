from dotenv import load_dotenv
import os

load_dotenv(".env.example")

class WignerCipher:
    ALPHABET = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    def __init__(self, key: str = None):
        self.key = key.lower() if key else os.getenv("KEY")

    def get_char_index(self, char: str) -> int:
        return self.ALPHABET.index(char.lower())

    def get_key_char_index(self, key_index: int) -> int:
        return self.ALPHABET.index(self.key[key_index % len(self.key)])

    def get_symbol(self, shift: int, is_upper: bool) -> str:
        symbol = self.ALPHABET[shift % len(self.ALPHABET)]
        return symbol.upper() if is_upper else symbol.lower()

    def encrypt(self, plaintext: str) -> str:
        encrypted_text = []
        key_index = 0

        for char in plaintext:
            if char in self.ALPHABET:
                char_index = self.get_char_index(char=char)
                key_char_index = self.get_key_char_index(key_index=key_index)

                shift = char_index + key_char_index

                encrypted_symbol = self.get_symbol(shift=shift, is_upper=char.isupper())
                encrypted_text.append(encrypted_symbol)
                key_index += 1
            else:
                encrypted_text.append(char)

        return "".join(encrypted_text)

    def decrypt(self, encrypted_text: str) -> str:
        decrypted_text = []
        key_index = 0

        for char in encrypted_text:
            if char in self.ALPHABET:
                char_index = self.get_char_index(char=char)
                key_char_index = self.get_key_char_index(key_index=key_index)

                shift = char_index - key_char_index
                decrypted_symbol = self.get_symbol(shift=shift, is_upper=char.isupper())
                decrypted_text.append(decrypted_symbol)
                key_index += 1
            else:
                decrypted_text.append(char)

        return "".join(decrypted_text)
