#Uncomment line above & run cell to save solution
#TODO Define class that implements securityInterface & allows for the management of a security
#filename interfaces.securityInterface.py
#Security Class Interface

        
class security():
    def __init__(self, name: str) -> None:
        self.name = name
    
    def getName(self) -> str:
        return self.name
        
    def setName(self, name) -> str:
        self.name = name