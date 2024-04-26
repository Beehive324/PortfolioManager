#Uncomment line above & run cell to save solution
#TODO Define class that implements accountInterface & allows for the management of an account
from interfaces.positionInterface import positionInterface
from implementations.securitySolution import security
from implementations.positionSolution import position
import random
from typing import Any, Dict, Set, Iterable

all_positions = []

class account():
    def __init__(self, positions: Set[positionInterface], accountName: str) -> None:
        self.positions = {position.getSecurity().getName(): position for position in positions} #position dict
        self.accountName = accountName #initialises account name

    def getName(self) -> str:
        return str(self.accountName) #returns the account name, passed
    """        
    Allow for the querying of all positions
    list comprehension to get all positions, shown as a list, passed
    """
    def getAllPositions(self) -> Iterable[positionInterface]:
        return list(self.positions.values())
        
    def getPositions(self, securities: Set) -> Dict[Any, positionInterface]:
        positions = {}
        for sec in securities:
            name = None
            if isinstance(sec, security):
                name = sec.getName()
            else:
                name = sec
            if name in self.positions:
                positions[sec] = self.positions[name]
                
        return positions 
    """
    Allow for positions to be added to the account with a set of position objects. 
    Incoming positions should update existing positions
    """
    def addPositions(self, positions: Set[positionInterface]) -> None:
        for position in positions:
            self.positions[position.getSecurity().getName()] =  position #add the position

    def removePositions(self, securities: Set) -> None:
        for sec in securities:
            if isinstance(sec, security):
                self.positions.pop(sec.getName(), None)
            else:
                print(self.positions)
                self.positions.pop(sec, None)
                print(self.positions)
                
    def getCurrentMarketValue(self) -> float:
        return sum([pos.getCurrentMarketValue() for pos in self.positions.values()])
    def getCurrentFilteredMarketValue(self, securities: Set) -> float:
        return sum([pos.getCurrentMarketValue() for pos in self.getPositions(securities).values()])
