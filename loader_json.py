import json


class LoaderJson:
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, 'r') as file:
            sounds = json.load(file)
        return sounds
