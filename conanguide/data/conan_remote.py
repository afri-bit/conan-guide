class ConanRemote:
    def __init__(self, name: str, url: str, ssl: bool):
        self.name = name
        self.url = url
        self.ssl = ssl