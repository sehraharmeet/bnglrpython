import json
import os

from Helper import JsonHelper
from TraderStock import TraderStock
from InvestorStock import InvestorStock
from SubMenuDisplay import SubMenuDisplay


Investor_File_Name = "Investor.json"
Stock_File_Name = "Stocks.json"

class Investor:
    def __init__(self, investorName,Fund,avaliableFund,investedCompanies):
        self.investorName = investorName
        self.Fund = Fund
        self.AvaliableFund =avaliableFund 
        self.InvestedCompanies = investedCompanies

    # def AddInvestmentFund(self,fund):
    #     self.Fund+=fund

    # def ReturnInvestmentFund(self,fund):
    #     return self.Fund
    
    # def AddInvestedCompanyDetails(self,stock):
    #     self.InvestedCompanies.append(stock)
    
    # def ReturnInvestedCompanyDetails(self):
    #     return self.InvestedCompanies
    
    @staticmethod
    def addInvestor():
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        print("\n")
        investorName = input("Enter the Investor Name to be added to the system: ")
        fund = int(input("Enter the Intial amount for: "))
        
        if not Investor.checkForDuplicateInvestorNames(investorName):
            existing_data.append(Investor(investorName,fund,fund,[]).__dict__)
            JsonHelper.save_Json(Investor_File_Name,existing_data)
            print ( " === INVESTOR SUCCESSFULLY ADDED ===  \n")
        print ("\n")
        menuHelper()
        # selectOption = input("Do you want to go the main menu --- click YES or NO:  ")
        # if selectOption.upper() == "NO":
        #     JsonHelper.SubMenuForInvestor()
        #     selectSubOption = input("Select Option : ")
        #     if selectSubOption == "1":
        #         Investor.addInvestor()
        #     else:
        #         Investor.buyStocks()
        # else:
        #     JsonHelper.GoToMainMenu()
        #     selectOption = input("Select Option: ")
        #     if selectOption == "1":
        #          SubMenuDisplay.displayeSubMenuForAdmin()
        #          #JsonHelper.callingEditStockPriceFromAdmin()
        #     elif selectOption == "2":
        #         SubMenuDisplay.displayeSubMenuForInvestor()
        #         print("\n\n")
        #         selectSubOption = input("Select Option : ")
        #         if selectSubOption == "1":
        #              Investor.addInvestor()
        #         else:
        #              Investor.buyStocks()    
        #     elif selectOption == "3":
        #             print("\nAdd New stock details")
        #             TraderStock.addStockDetails()
        #             print("\n")
        #     elif selectOption == "4":
        #         print("\nExited the App\n\n\n")




    @staticmethod
    def checkForDuplicateInvestorNames(investorNameParam):
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        isInvestorNameAvailable = False
        for invobj in existing_data:
            if invobj["investorName"].upper() == investorNameParam.upper():
                print("\n ***  Duplicate Investor Names not allowed *** ")
                isInvestorNameAvailable = True
                break
        return isInvestorNameAvailable        
        




    @staticmethod
    def buyStocks():
        existing_data = JsonHelper.load_Json(Stock_File_Name)
        investorName=""
        if len(existing_data)<1:
            print("No Stock Exists in the System")    
        else:  
           investorName = input("Enter Investor Name: ")
           if not checkIfTheInvestorExists(investorName):
               print(" The Entered Investor Name doesn't exists in DB ")
               menuHelper()

           else: 
            stockName = input("Enter stock name to be purchased: ")
            isStockEnterMatch = False          
            for stk in existing_data:
                if stk["StockName"].upper() == stockName.upper():
                        isStockEnterMatch = True
                        if int(stk["totalnumberOfStocks"]) -int(stk["soldStock"]) > 0 :
                            leftOverStock = int(stk["totalnumberOfStocks"]) -int(stk["soldStock"])
                            print(f" The total number of stocks available for purchase is {leftOverStock} at the rate {stk["eachStock"]} each ")
                            StockCntTobePurchased= int(input("Enter the count of stocks to be purchased: "))
                            isSufficentFundAvailable = Investor.checkIfFundsAvailableForPurchaseStock(investorName,(StockCntTobePurchased*int(stk["eachStock"])))
                            if isSufficentFundAvailable:
                                Investor.updateTraderStockJsonFile(existing_data,stk,StockCntTobePurchased)
                                Investor.updateInvestorStockJsonFile(investorName,stk["StockName"],StockCntTobePurchased,stk["eachStock"])
                                print ("STOCKS SUCCESFULLY PURCHASED  \n")
                            else:
                                print ("INSUFFICIENT BALANCE TO BUY STOCKS")    
                        break
            if isStockEnterMatch == False:
                print("No stock with the entered name exists in the DB")
            menuHelper()   

             

    @staticmethod
    def updateTraderStockJsonFile(existing_data,stockToUpdate,StockCntTobePurchased):
        updated_data =[]
        
        for stk in existing_data:
            
            if stk["StockName"] != stockToUpdate["StockName"]:
                updated_data.append(TraderStock(stk["StockName"],stk["totalnumberOfStocks"],stk["eachStock"],stk["soldStock"]).__dict__)
                
            else:
               
                soldStock = int(stk["soldStock"]) + StockCntTobePurchased
                updated_data.append(TraderStock(stk["StockName"],stk["totalnumberOfStocks"],stk["eachStock"],soldStock).__dict__)
                
        JsonHelper.save_Json(Stock_File_Name,updated_data)   

    @staticmethod
    def checkIfFundsAvailableForPurchaseStock(investorName,totalStockValue):
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        for invObj in existing_data:
            if int(invObj["Fund"]) > totalStockValue:
                return True
            else:
                return False

    @staticmethod
    def updateInvestorStockJsonFile(investorName,stockName,StockCntTobePurchased,purchasedStockPrice):
        
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        updated_data =[]
        investedStocks = []
        for stk in existing_data:
            
            if stk["investorName"] != investorName:
                print(f'test this {stk["AvaliableFund"]}')
                updated_data.append(Investor(stk["investorName"],stk["Fund"],stk["AvaliableFund"],stk["InvestedCompanies"]).__dict__)
                
                
            else:
                isAdded = False
                for invStk in stk["InvestedCompanies"]:
                    isAdded = True
                    if invStk["stockName"].upper() != stockName.upper():
                        investedStocks.append(InvestorStock(invStk["stockName"],invStk["totalnumberOfStocks"],invStk["eachStock"],invStk["currentStockPrice"]).__dict__)
                    else:
                        investedStocks.append(InvestorStock(invStk["stockName"],(int(StockCntTobePurchased)+invStk["totalnumberOfStocks"]),purchasedStockPrice,purchasedStockPrice).__dict__)
                if not isAdded:
                   investedStocks.append(InvestorStock(stockName,int(StockCntTobePurchased),purchasedStockPrice,purchasedStockPrice).__dict__) 

                currentAvailableFund = stk["AvaliableFund"] - (int(StockCntTobePurchased) *int(purchasedStockPrice))
                updated_data.append(Investor(stk["investorName"],stk["Fund"],currentAvailableFund,investedStocks).__dict__)
                
        
        JsonHelper.save_Json(Investor_File_Name,updated_data)   

@staticmethod
def menuHelper():
        selectOption = input("Do you want to go the main menu --- click YES or NO:  ")
        if selectOption.upper() == "NO":
            JsonHelper.SubMenuForInvestor()
            selectSubOption = input("Select Option : ")
            if selectSubOption == "1":
                Investor.addInvestor()
            else:
                Investor.buyStocks()
        else:
            JsonHelper.GoToMainMenu()
            selectOption = input("Select Option: ")
            if selectOption == "1":
                 SubMenuDisplay.displayeSubMenuForAdmin()
                 #JsonHelper.callingEditStockPriceFromAdmin()
            elif selectOption == "2":
                SubMenuDisplay.displayeSubMenuForInvestor()
                print("\n\n")
                selectSubOption = input("Select Option : ")
                if selectSubOption == "1":
                     Investor.addInvestor()
                else:
                     Investor.buyStocks()    
            elif selectOption == "3":
                    print("\nAdd New stock details")
                    TraderStock.addStockDetails()
                    print("\n")
            elif selectOption == "4":
                print("\nExited the App\n\n\n")


@staticmethod
def checkIfTheInvestorExists(investorName):
        
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        isInvestorNameExists = False
        for invObj in existing_data:
            if invObj["investorName"].upper() == investorName.upper():
                isInvestorNameExists=True
                break
        return isInvestorNameExists   

@staticmethod
def sellInvestorStock():
        existing_Investor_data = JsonHelper.load_Json(Investor_File_Name)
        existing_Stock_data = JsonHelper.load_Json(Stock_File_Name)
        stockName=""
        investorName =""
        if len(existing_Stock_data)<1:
            print("No Stock Exists in the System")    
        else:  
           investorName = input("Enter Investor Name: ")
           if not checkIfTheInvestorExists(investorName):
               print(" The Entered Investor Name doesn't exists in DB ")
               menuHelper()

           else: 
            stockName = input("Enter stock name to be sold: ")
            stockcount = int(input("Enter the number of stocks to be sold: "))
            isStockAvailable = False
            for invObj in existing_Investor_data:
                if invObj["investorName"].upper() == investorName.upper():
                    for stkObj in invObj["InvestedCompanies"]:
                        if stkObj["stockName"].upper() == stockName.upper():
                            isStockAvailable = True
                            print(f'The investor holds stkObj["totalnumberOfStocks"] stocks of the stock {stockName}')
                            if stockcount > int(stkObj["totalnumberOfStocks"]):
                                print("The entered stock count to be sold is greater than the total number of stocks held")
                            else:
                                Investor.IncreaseTraderStockCount(existing_Stock_data,stockName,stockcount)
                                Investor.DecreaseInvestedStockCount(existing_Investor_data,investorName,stockcount,stockName)
                            break
                    if not isStockAvailable:
                       print ("The Entered stock name doesn't exist for the investor")               

              
                
@staticmethod
def IncreaseTraderStockCount(existing_Stock_data,stockName,stockcount):
    Updated_Stock_data = []
    for stkObj in existing_Stock_data:
        if stockName.upper() == stkObj["StockName"]:
          updatedStockCount = (int(stkObj["totalnumberOfStocks"]) + int(stockcount)) 
          Updated_Stock_data.append(TraderStock(stkObj["StockName"],stkObj["totalnumberOfStocks"],stkObj["eachStock"],stkObj["soldStock"]).__dict__)
        else:
            Updated_Stock_data.append(TraderStock(stkObj["StockName"],stkObj["totalnumberOfStocks"],stkObj["eachStock"],stkObj["soldStock"]).__dict__)

@staticmethod
def DecreaseInvestedStockCount(existing_Investor_data,investorName,stockcount,stockName):
    Updated_Investor_data = []
    for invObj in existing_Investor_data:
        if invObj["investorName"].upper == investorName.upper():
            updatedInvestedStocks= []
            for stkObj in invObj["InvestedCompanies"]:
                if stkObj["stockName"].upper() != stockName.upper():
                    updatedInvestedStocks.append(InvestorStock(stkObj["stockName"],stkObj["totalnumberOfStocks"],stkObj["eachStock"],stkObj["currentStockPrice"]).__dict__)
                else:
                    updatedStockCount = int(stkObj["totalnumberOfStocks"]) - int(stockcount)
                    if (updatedStockCount !=0):
                        updatedInvestedStocks.append(InvestorStock(stkObj["stockName"],stkObj["totalnumberOfStocks"],stkObj["eachStock"],stkObj["currentStockPrice"]).__dict__)
                        Updated_Investor_data.append(Investor(invObj["investorName"],invObj["Fund"],invObj["AvaliableFund"],updatedInvestedStocks).__dict__)
        else:
            Updated_Investor_data.append(Investor(invObj["investorName"],invObj["Fund"],invObj["AvaliableFund"],invObj["InvestedCompanies"]).__dict__)
                

    
