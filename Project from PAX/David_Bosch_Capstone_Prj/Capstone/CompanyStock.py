class CompanyStock:
    def __init__(self, companyName,totalnumberOfStocks,eachStock):
        self.totalnumberOfStocks = totalnumberOfStocks      # inValuestance variable
        self.eachStock = eachStock
        self.companyName=companyName
        self.soldStock= 0

    def getleftOverStock(self):
        return self.totalnumberOfStocks - self.soldStock
    
    def soldStock(self, noOfstocksSold):
         self.soldStock = (self.soldStock+ noOfstocksSold)
         return self.soldStock
    
    def updateStockValue(self, updatestockvalue):
         self.eachStock = updatestockvalue
         