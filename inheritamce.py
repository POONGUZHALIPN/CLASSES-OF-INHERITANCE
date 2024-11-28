class Inventory:
    def __init__(self):
        self.prodID=int(input("Enter a valid ID:"))
        self.prodName=input("Enter your name:")
        self.prodCount=int(input("Enter the count:"))
class showinfo(Inventory):
    def show(self):
        print("ID=",self.prodID,"\n","NAME=",self.prodName,"\n","COUNT=",self.prodCount)

s=showinfo()
s.show()


class Inventory:
    def __init__(self,prodName,prodID,prodCount):
        self.prodID=prodID
        self.prodName=prodName
        self.prodCount=prodCount
    def show(self):
        print("ID:", self.prodID)
        print("NAME:",self.prodName)
        print("COUNT:",self.prodCount)
s=Inventory("poongu",344,6)
s.show()

class Employee:
    def getEmployeeInfo(self):
        self.id=input("Enter the ID:")
        self.name=input("Enter the Name:")
    def displayEmployeeInfo(self):
        print("ID=",self.id,"\n Name=",self.name)
class Perks(Employee):
    def getDetails(self):
        self.sal=int(input("Enter the Salary:"))
    def displayInfo(self):
        print("salary=",self.sal)
p=Perks()
p.getDetails()
p.displayInfo()
























