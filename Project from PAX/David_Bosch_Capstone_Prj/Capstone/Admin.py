import json
import os

from Helper import JsonHelper
from TraderStock import TraderStock
from InvestorStock import InvestorStock
from Investor import Investor
from colorama import  Fore, Style, init

# from Main import Main


Stock_File_Name = "Stocks.json"
Investor_File_Name = "Investor.json"

class Admin:

    @staticmethod
    def EditStockPrice():
        existing_data = JsonHelper.load_Json(Stock_File_Name)
        if existing_data.count == 0:
            print("No Stock exists in the DB")    
        else:  
           stockName = input("Enter the stock name for the price to be edited: ")
           isStockEnterMatch = False          
           for stk in existing_data:
             if stk["StockName"].upper() == stockName.upper():
                    isStockEnterMatch = True
                    print(f"The current stock price for the entered stock name {stk["StockName"].upper()} is {stk["eachStock"]}:  ")
                    newStockPrice = input("Enter the New stock price: ")
                    Admin.UpdateStockJson(existing_data,stockName,newStockPrice)
                    Admin.UpdateInvestorJson(stockName,newStockPrice)

                    break
           if isStockEnterMatch == False:
               print("No Stock matches with the entered name ")

        # Main.MyMain()
    
    @staticmethod
    def UpdateStockJson(existing_data,stockName,newStockPrice):
        updated_data = []
        for stk in existing_data:
            if stk["StockName"].upper() != stockName.upper():
                updated_data.append(TraderStock(stk["StockName"],stk["totalnumberOfStocks"],stk["eachStock"],stk["soldStock"]).__dict__)
            else:
                updated_data.append(TraderStock(stk["StockName"],stk["totalnumberOfStocks"],newStockPrice,stk["soldStock"]).__dict__)
       
        JsonHelper.save_Json(Stock_File_Name,updated_data)           

    @staticmethod
    def UpdateInvestorJson(stockName,newStockPrice):
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        updated_data = []

        for inv in existing_data:
            invStock= []
            for invStk in inv["InvestedCompanies"]:
                if invStk["stockName"] != stockName :
                     invStock.append(InvestorStock(invStk["stockName"],invStk["totalnumberOfStocks"],invStk["eachStock"],invStk["currentStockPrice"]).__dict__)
                else:
                    invStock.append(InvestorStock(invStk["stockName"],invStk["totalnumberOfStocks"],invStk["eachStock"],newStockPrice).__dict__)

            
            updated_data.append(Investor(inv["investorName"],inv["Fund"],inv["AvaliableFund"],invStock).__dict__)    
           
       
        JsonHelper.save_Json(Investor_File_Name,updated_data)
        print ("\n STOCK PRICE SUCESSFULLY UPDATED ACROSS THE SYSTEM")               

    @staticmethod
    def ListOfAllInvestors():
        print("ListofAllInvestors\n")
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        for invObj in existing_data:
            print(f"Investor Name: {invObj["investorName"]} Started with Initial Fund: {invObj["Fund"]} \n")

    @staticmethod
    def DetailListOfSingleInvestor(investorName):
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        isInvestorExists = False
        for invObj in existing_data:
            if invObj["investorName"].upper() == investorName.upper():
                isInvestorExists = True
                print(f"Investor Name: {invObj["investorName"]} \n")
                for stk in invObj["InvestedCompanies"]:
                    print(f"Invested in Stock: {stk["stockName"]} and total Count of Stocks Held: {stk["totalnumberOfStocks"]} \n") 
        if not isInvestorExists:
           print("Entered Investor Name doesn't exists in the system")  

    @staticmethod
    def PortfoliaStatusOfAnInvestor(investorName):
        existing_data = JsonHelper.load_Json(Investor_File_Name)
        isInvestorExists = False
        for invObj in existing_data:
            if invObj["investorName"].upper() == investorName.upper():
                isInvestorExists = True
                print(f"Investor Name: {invObj["investorName"]} \n")
                currentStockValue =0
                print (Fore.MAGENTA +"PORTFOLIO LOSS/PROFIT STATEMENT:")
                for stk in invObj["InvestedCompanies"]:
                    currentStockValue+= int(stk["totalnumberOfStocks"]) * int(stk["currentStockPrice"])
                    orinalStockValue = int(stk["totalnumberOfStocks"]) * int(stk["eachStock"])
                    if int(orinalStockValue) == int(currentStockValue):
                        print(Fore.MAGENTA +f"The Stock {stk["stockName"]} is having a no profit or loss \n")
                    elif int(orinalStockValue) < int(currentStockValue):
                        print(Fore.MAGENTA +f"The Stock {stk["stockName"]} is having a profit of {(int(currentStockValue) - int(orinalStockValue))} \n")
                    else:
                        print(Fore.MAGENTA + f"The Stock {stk["stockName"]} is having a loss of {(int(currentStockValue) - int(orinalStockValue))} \n")    
                       
        if not isInvestorExists:
           print("Entered Investor Name doesn't exists in the system")         