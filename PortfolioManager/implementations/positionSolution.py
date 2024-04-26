#Uncomment line above & run cell to save solution
#TODO Define class that implements positionInterface & allows for the management of a position
import os
import sys
module_path = os.path.abspath('..')
if module_path not in sys.path:
    sys.path.append(module_path)

from implementations.securitySolution import security
from interfaces.securityInterface import securityInterface
from generators.priceDataGenerator import priceData

class position():
    def __init__(self, security_name, initialPosition: int) -> None:
        #if its a string , create security with the name -> security_name
        if isinstance(security_name, str):
            security_obj = security(security_name)
            self.security = security_obj
        #if its an object return the object
        else:
            self.security = security_name
            
        #initialise security variable
        self.initialPosition = initialPosition #initialise inital Position

    def getSecurity(self) -> securityInterface:
        return self.security
        
    def getPosition(self) -> int:
        return self.initialPosition
        
    def setPosition(self, inputValue: int) -> None:
        if inputValue < 0:
            raise Exception
        self.initialPosition = inputValuee
        
    def addPosition(self, inputValue: int) -> None:
        if self.initialPosition + inputValue < 0:
            raise Exception
        self.initialPosition += inputValue
        
    def getCurrentMarketValue(self) -> float:
        #self.initialPosition
        #self.security
        #LASTEST_EXPECTED_MV = EXPECTED_POSITION_AMOUNT * DATA_SOURCE.getSecurityPriceDataList(EXPECTED_NAME)[-1]
        sec_objs = security(self.security.getName())
        result = sec_objs.getCurrentMarketValue() * self.initialPosition
        return result
        
