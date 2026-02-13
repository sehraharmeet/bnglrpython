import json
import os

# from Investor import Investor
from SubMenuDisplay import SubMenuDisplay
from MainMenuDisplay import MainMenuDisplay
# from Admin import Admin


class JsonHelper:

    @staticmethod
    def load_Json(FILE_NAME):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    @staticmethod
    def save_Json(FILE_NAME,data):
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def SubMenuForInvestor():
        SubMenuDisplay.displayeSubMenuForInvestor()
        print("\n\n")
        
    @staticmethod
    def GoToMainMenu():
        MainMenuDisplay.displayeMainMenu()
        print("\n\n")

    

        