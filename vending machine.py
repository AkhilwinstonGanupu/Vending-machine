import mysql.connector
db=mysql.connector.connect(host="localhost",user="root",password="Akhil@123")
c=db.cursor()

c.execute("Use VM")



class Coin(object):
    def __init__(self,denom,value):
        self.Denomination = "CENTS"
        self.Value = 0
        if value == 25 or value == 50:
            self.Value = value

    def getValue(self):
        return self.Value

    def setValue(self,v): 
        self.Value = 0
        if value == 25 or value == 50:
            self.Value = value
    def getDenomiation(self):
        return self.Denomination

    def setDenomination(self, d):
        self.Denomination = d
        
    def __str__(self):
        return str(self.Value)+" " + self.Denomination

class Item(object):
    def __init__(self,n,c,p,q):
        self.Name = n
        self.Code = c
        self.Price = p
        self.Quantity = q
    def getName(self):
        return self.Name
    def setName(self,n):
        self.Name = n

    def getCode(self):
        return self.Code
    def setCode(self,n):
        self.Code = n
    def getPrice(self):
        return self.Price
    def setPrice(self,n):
        self.Price = n
    def getQuantity(self):
        return self.Quantity
    def setQuantity(self,n):
        self.Quantity = n

    def __str__(self):
        output = "Name: " + self.Name
        output += "\nCode: " + self.Code
        output += "\nPrice: " + str(self.Price)
        output += "\nQuantity: " + str(self.Quantity)
        return output

    
class VendingMachine(object):
    def __init__(self):
        self.allItems = []
        self.amount = 0

    def getItems(self):
        return self.allItems

    def getAmount(self):
        return self.amount
    def setAmount(self,a):
        self.amount = a

    def addItem(self, It):
        for i in self.allItems:
            if i.getCode() == It.getCode():
                i.setQuantity(i.getQuantity() + It.getQuantity())
                return
        self.allItems.append(It)

    def insertCoin(self, cn):
        if cn.getValue() == 25 or  cn.getValue() == 50:
            self.amount += cn.getValue()*1.0/100
    def vendItem(self,code):
        for i in self.allItems:
            if i.getCode() == code:
                if i.getQuantity() > 0:
                    if self.getAmount() >= i.getPrice():
                        self.setAmount(self.getAmount() - i.getPrice())
                        i.setQuantity(i.getQuantity() - 1)
                        print("Name: " + i.Name)
                        print("Code: " + str(i.Code))
                        print("Price: " + str(i.Price))
                    else:
                        print("Not Enough Money to Buy " + i.getName() )
                    
                else:
                    print("Quantity Out of Stock")
                return
        print("Item with Code " + str(code)+" does not exist")

    def returnBalance(self):
        print("Amount Returned = "+str(self.getAmount()))
        self.setAmount(0)


def printMenu():
    
    print(" ____________________________\n","|Menu                      |","\n",
    "|--------------------------|","\n",
    "|  1. Stock an Item        |","\n",
    "|  2. Display all Items    |","\n",
    "|  3. Insert 25 cents      |","\n",
    "|  4. Insert 50 cents      |","\n",
    "|  5. Buy Item             |","\n",
    "|  6. Get Change           |","\n",
    "|  7. Print Current Amount |","\n",
    "|  8. Exit                 |","\n",
    "|__________________________|","\n",)


def StockItem(Vm):
    passw =123
    p=int(input("Enter admin pasword:"))
    if p==passw:
        name = input("Enter Name of Item:")
        price = float(input("Enter Price: "))
        code = input("Enter Code: ")
        quantity = int(input("Enter Quantity: "))
        itm = {"name":name,"code":code,"price":price,"quantity":quantity}
        Vm.addItem(itm)
        c.execute("Insert into stock values(name,price,code,quantity);")
    else:
        print("password incorrect only admins are allowed to stock")
def DisplayAllItems(Vm):
    c.execute("select * from stock;")
    row=c.fetchall()
    for i in row:
        print(i)
    c.execute("commit;")
    
def Insert25Cents(Vm):
    inp=int(input("Enter userid:"))
    c.execute("select from acc where inp==userid;")        
    C25 = Coin("cents",25)
    Vm.insertCoin(C25)

def Insert50Cents(Vm):
    iup=int(input("Enter userid:"))
    c.execute("select from acc where iup==userid:")
    C50 = Coin("cents",50)
    Vm.insertCoin(C50)

def BuyItem(Vm):
    code =input("Enter Code of Item you want to buy> ")
    Vm.vendItem(code)

def GetChange(Vm):
    Vm.returnBalance()
    
def PrintAmt(Vm):
    print("Current Amount is "+str(Vm.getAmount()))

inp = 0
Vmach = VendingMachine()
while inp != 8:
    printMenu()
    inp = int(input("Enter your choice> "))
    if inp == 1:
        StockItem(Vmach)
    elif inp == 2:
        DisplayAllItems(Vmach)
    elif inp == 3:
        Insert25Cents(Vmach)
    elif inp == 4:
        Insert50Cents(Vmach)
    elif inp == 5:
        BuyItem(Vmach)
    elif inp == 6:
        GetChange(Vmach)
    elif inp == 7:
        PrintAmt(Vmach)
    elif inp == 8:
        print("Thank you for your business")


 
