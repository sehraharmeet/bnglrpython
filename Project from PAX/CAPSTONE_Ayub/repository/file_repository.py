import json


class FileRepository:

    @staticmethod
    def load_data(filepath):
        try:
            with open(filepath, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    @staticmethod
    def save_data(filepath, data):
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
