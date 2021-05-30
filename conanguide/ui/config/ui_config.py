import os
import stat
import json


class UIConfiguration:
    def __init__(self):
        self.config = dict()
        self.config_name = "config.json"
        self.config_location = os.path.join(os.path.expanduser("~"), os.path.normpath(".conanguide"))
        self.config_full_path = os.path.join(self.config_location, self.config_name)

    def get_config_location(self) -> str:
        return self.config_location

    def load_config(self):
        if os.path.isfile(self.config_full_path):
            with open(self.config_full_path, "r") as f:
                self.config = json.loads(f.read())
        else:
            return None
        return self.config

    def save_config(self) -> None:
        if not os.path.isdir(self.config_location):
            os.mkdir(self.config_location)

        with open(self.config_full_path, "w+") as f:
            f.write(json.dumps(self.config, indent=2))

        os.chmod(self.config_full_path, stat.S_IWRITE)

    def clear_config(self):
        self.config.clear()

    def add_header(self, name: str):
        self.config[name] = dict()

    def add_value(self, key: str, value, header=None):
        if header is None:
            self.config[key] = value
        else:
            self.config[header][key] = value
