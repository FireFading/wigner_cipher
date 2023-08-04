import argparse

from core.service import WignerCipher
from core.saver import Saver


class CommandManager:
    def __init__(self):
        self.is_decrypt, key, language, need_to_save = self.get_args()
        self.text = input("Enter text: ")
        self.service = WignerCipher(key=key, language=language)
        self.saver = None
        if need_to_save:
            filename = "decrypted.txt" if self.is_decrypt else "encrypted.txt"
            self.saver = Saver(filename=filename)

    def get_args(self):
        parser = argparse.ArgumentParser(description="Encrypt and Decrypt")
        parser.add_argument(
            "-d",
            "--decrypt",
            action="store_true",
            default=False,
            help="Decrypt encrypted text",
        )
        parser.add_argument("-k", "--key", type=str, default=None, help="Key to encrypt/decrypt")
        parser.add_argument(
            "-l",
            "--language",
            type=str,
            default="russian",
            choices=["russian", "english"],
            help="Language to encrypt/decrypt",
        )
        parser.add_argument("-s", "--save", action="store_true", default=False, help="Save result to file")
        args = parser.parse_args()
        return args.decrypt, args.key, args.language, args.save

    def run(self):
        if not self.is_decrypt:
            result = self.service.encrypt(plaintext=self.text)
        else:
            result = self.service.decrypt(encrypted_text=self.text)
        if self.saver:
            self.saver.write(data=result)
        return result
