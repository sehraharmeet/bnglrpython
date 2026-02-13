from CompanyStock import CompanyStock
from Investor import Investor
from InvestorStock import InvestorStock
from MainMenuDisplay import MainMenuDisplay
from SubMenuDisplay import SubMenuDisplay
from TraderStock import TraderStock
from Admin import Admin


class Main:
        
    #  @staticmethod    
    #  def MyMain():
      
        MainMenuDisplay.displayeMainMenu()
        selectOption = input("Select Option: ")

        if selectOption == "1":
            SubMenuDisplay.displayeSubMenuForAdmin()
            selectSubOption = input("Select Option : ")
            if selectSubOption == "1":
                Admin.EditStockPrice()
            elif selectSubOption == "2":
                 Admin.ListOfAllInvestors()
            elif selectSubOption == "3":
                 investorName = input("Enter the Name of the Investor: ")
                 Admin.DetailListOfSingleInvestor(investorName)     
            elif selectSubOption == "4":
                 investorName = input("Enter the Name of the Investor: ")
                 Admin.PortfoliaStatusOfAnInvestor(investorName)              
        elif selectOption == "2":
            SubMenuDisplay.displayeSubMenuForInvestor()
            print("\n\n")
            selectSubOption = input("Select Option : ")
            if selectSubOption == "1":
                Investor.addInvestor()
            elif selectSubOption == "2":
                Investor.buyStocks()
            elif selectSubOption == "3":
                Investor.sellInvestorStock()
            else:    
                print("Exited App") 

        elif selectOption == "3":
            print("\n ------ Add New stock details ------- \n")
            SubMenuDisplay.displayeSubMenuForTrader()
            selectSubOption = input("Select Option : ")
            if selectSubOption == "1":
                TraderStock.addStockDetails()
            elif selectSubOption == "2":
                TraderStock.editExistingStockDetails()    
            print("\n")
        elif selectOption == "4":
            print("\nExited the App\n\n\n")



# Main.MyMain()
@staticmethod
def callingEditStockPriceFromMain():
        Admin.EditStockPrice()