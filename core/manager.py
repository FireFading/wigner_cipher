import argparse
from core.service import WignerCipher


class CommandManager:
    def __init__(self):
        self.is_decrypt = self.get_args()
        self.text = input("Enter text: ")
        key = input("Enter key: ")
        self.service = WignerCipher(key=key)

    def get_args(self):
        parser = argparse.ArgumentParser(description="Encrypt and Decrypt")
        parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt encrypted text")
        args = parser.parse_args()
        return args.decrypt

    def run(self):
        if not self.is_decrypt:
            return self.service.encrypt(plaintext=self.text)
        return self.service.decrypt(encrypted_text=self.text)
