#Uncomment line above & run cell to save solution
#TODO Define class that implements portFolioInterface & allows for the management of a portfolio
from typing import Set, Iterable
from interfaces.accountInterface import accountInterface
from interfaces.securityInterface import securityInterface
from implementations.securitySolution import security
from implementations.positionSolution import position
from implementations.accountSolution import account

class portfolio():
    def __init__(self, portfolioName: str, accounts: Set[accountInterface]) -> None:
        self.portfolioName = portfolioName
        self.accounts = {account.getName(): account for account in accounts} #dict comprehension

    def getAllAccounts(self) -> Iterable[accountInterface]: #passed
        return list(self.accounts.values()) #list of values in the dictionary
    

    def getAccounts(self, accountNamesFilter:Set[str], securitiesFilter:Set) -> Iterable[accountInterface]: 
        list_accounts = []
        for account in list(self.accounts.values()):
            if account in accountNamesFilter:
                list_accounts.append(account)
        return list_accounts

    def addAccounts(self, accounts: Set[accountInterface]) -> None:
        for acc in accounts:
            self.accounts[acc.getName()] = acc #adds to the dictionary

    def removeAccounts(self, accountNames: Set[str]) -> None:
        for accountname in accountNames:
            self.accounts.pop(accountname, None) #removes from the dictionary
            
        
