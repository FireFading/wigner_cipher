class Saver:
    def __init__(self, filename: str = "encrypted.txt"):
        self.filename = filename

    def write(self, data: str):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(data)
