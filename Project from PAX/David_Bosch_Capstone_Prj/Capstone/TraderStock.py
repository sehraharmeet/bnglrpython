import json
import os

from Helper import JsonHelper
from SubMenuDisplay import SubMenuDisplay

FILE_NAME = "Stocks.json"


class TraderStock:
    def __init__(self,StockName,totalnumberOfStocks,eachStockprice,soldStock):
        self.StockName = StockName
        self.totalnumberOfStocks = totalnumberOfStocks      # inValuestance variable
        self.eachStock = eachStockprice
        self.soldStock = soldStock
        

    def getleftOverStock(self):
        return self.totalnumberOfStocks - self.soldStock
    
    def soldStock(self, noOfstocksSold):
         self.soldStock = (self.soldStock+ noOfstocksSold)
         return self.soldStock
    
    def updateStockValue(self, updatestockvalue):
         self.eachStock = updatestockvalue

    @staticmethod
    def addStockDetails():
        existing_data = JsonHelper.load_Json(FILE_NAME)
        stockName = input("Enter the stock Name: ")
        if not TraderStock.checkforDuplicateStock(stockName):
            totalnumberOfStocks = int(input("Enter the total number of stocks: "))
            eachStockprice = int(input("Enter the cost of each stock: "))
            existing_data.append(TraderStock(stockName,totalnumberOfStocks,eachStockprice,0).__dict__)
            JsonHelper.save_Json(FILE_NAME,existing_data)
        else:
            print("The Entered stock name already exists in the DB")        


    @staticmethod
    def checkforDuplicateStock(stockName):
        existing_data = JsonHelper.load_Json(FILE_NAME)
        isDuplicateStockExist = False
        for stk in existing_data:
            if stk["StockName"].upper() == stockName.upper():
                isDuplicateStockExist = True
                break 
        return isDuplicateStockExist

    @staticmethod
    def editExistingStockDetails():
        existing_data = JsonHelper.load_Json(FILE_NAME)
        updated_data =[]
        stockName = input("Enter the stock Name: ")
        if TraderStock.checkforDuplicateStock(stockName):
            totalnumberOfStocks = int(input("Enter the total number of stocks to be maintained: "))
            isTobeUpdatedInDB = True
            for stkObj in existing_data:
                if stkObj["StockName"].upper() == stockName.upper():
                    if totalnumberOfStocks >=stkObj["soldStock"]:
                         updated_data.append(TraderStock(stkObj["StockName"],totalnumberOfStocks,stkObj["eachStock"],stkObj["soldStock"]).__dict__)
                    else:
                        print("Total number of stocks to be maintained cannot be less than the stocks solde")
                        isTobeUpdatedInDB = False     
                else:    
                    updated_data.append(TraderStock(stkObj["StockName"],stkObj["totalnumberOfStocks"],stkObj["eachStock"],stkObj["soldStock"]).__dict__)
            if isTobeUpdatedInDB:
                JsonHelper.save_Json(FILE_NAME,updated_data)
        else:
            print("The Entered stock name doesn't exits in the DB")        
    

# @staticmethod
# def menuHelper():
#         selectOption = input("Do you want to go the main menu --- click YES or NO:  ")
#         if selectOption.upper() == "NO":
#             print("\n ------ Add New stock details ------- \n")
#             SubMenuDisplay.displayeSubMenuForTrader()
#             selectSubOption = input("Select Option : ")
#             if selectSubOption == "1":
#                 TraderStock.addStockDetails()
#             elif selectSubOption == "2":
#                 TraderStock.editExistingStockDetails()    
#             print("\n")
#         else:
#             JsonHelper.GoToMainMenu()
#             selectOption = input("Select Option: ")
#             if selectOption == "1":
#                  SubMenuDisplay.displayeSubMenuForAdmin()
#                  #JsonHelper.callingEditStockPriceFromAdmin()
#             elif selectOption == "2":
#                 SubMenuDisplay.displayeSubMenuForInvestor()
#                 print("\n\n")
#                 selectSubOption = input("Select Option : ")
#                 if selectSubOption == "1":
#                     # Investor.addInvestor()
#                 else:
#                      Investor.buyStocks()    
#             elif selectOption == "3":
#                     print("\nAdd New stock details")
#                     TraderStock.addStockDetails()
#                     print("\n")
#             elif selectOption == "4":
#                 print("\nExited the App\n\n\n")