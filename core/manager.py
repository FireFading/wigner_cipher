import argparse
from core.service import WignerCipher


class CommandManager:
    def __init__(self):
        self.is_decrypt, key, language = self.get_args()
        self.text = input("Enter text: ")
        self.service = WignerCipher(key=key, language=language)

    def get_args(self):
        parser = argparse.ArgumentParser(description="Encrypt and Decrypt")
        parser.add_argument("-d", "--decrypt", action="store_true", default=False, help="Decrypt encrypted text")
        parser.add_argument("-k", "--key", type=str, default=None, help="Key to encrypt/decrypt")
        parser.add_argument("-l", '--language', type=str, default="russian", choices=["russian", "english"], help="Language to encrypt/decrypt")
        args = parser.parse_args()
        return args.decrypt, args.key, args.language

    def run(self):
        if not self.is_decrypt:
            return self.service.encrypt(plaintext=self.text)
        return self.service.decrypt(encrypted_text=self.text)
