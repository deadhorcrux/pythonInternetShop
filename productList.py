from classProduct import Product
from generalList import generalList
class productList(generalList):
    def getName(self, code):
        return self.findBycode(code).getName()
    def getPrice(self, code):
        return self.findBycode(code).getPrice()
    def getValue(self, code):
        return self.findBycode(code).getValue()
    def getinfo(self, code):
        return self.findBycode(code).info()
    def infolist(self):
        s=""
        for code in self.getCodes():
            s+=self.getinfo(code)+" "
            if s:s=s[:-2]
            return s
 
    def setName(self, code, name):
        self.findBycode(code).setName(name)
    def setPrice(self, code, price):
        self.findBycode(code).setPrice(price)
    def setValue(self, code, value):
        self.findBycode(code).setValue(value)
    def newRec(self, code, name, price, value):
        self.appendList(Product(code, name, price, value))
