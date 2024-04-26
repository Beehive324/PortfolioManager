#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
from generators.priceDataGenerator import priceData
class security():
    def __init__(self, name: str) -> None:
        self.name = name
    
    def getName(self) -> str:
        return self.name
        
    def setName(self, name) -> str:
        self.name = name
        
    def getCurrentMarketValue(self) -> float:
        pD = priceData()
        print("sec get current market val", self.name)
        curPrice = pD.getCurrentPrice(self.getName())
        print("sec get current market val cur price", curPrice)
        return curPrice
