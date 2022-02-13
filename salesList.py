from classSales import Sales
from generalList import generalList
class salesList(generalList):
    def getProduct(self, code):
        return self.findBycode(code).getProduct()
    def getClient(self, code):
        return self.findBycode(code).getClient()
    #def getClientCode(self, code):
     #   return self.findBycode(code).getCode()
    def getDate_of_sale(self, code):
        return self.findBycode(code).getDate_of_sale()
    def getValue(self, code):
        return self.findBycode(code).getValue()
    def getDelivery(self, code):
        return self.findBycode(code).getDelivery()
    def getinfo(self, code):
        return self.findBycode(code).info()
    def infolist(self):
        s=""
        for code in self.getCodes():
            s+=self.getinfo(code)+" "
            if s:s=s[:-2]
            return s
    def setProduct(self, code, product):
        self.findBycode(code).setProduct(product)
    def setClient(self, code, client):
        self.findBycode(code).setClient(client)
    def setDate_of_sale(self, code, date_of_sale):
        self.findBycode(code).setDate_of_sale(date_of_sale)
    def setDelivery(self, code, delivery):
        self.findBycode(code).setDelivery(delivery)
    def setValue(self, code, value):
        self.findBycode(code).setValue(value)
    def newRec(self, code, product, client,date_of_sale, delivery, value):
        self.appendList(Sales(code, product, client,date_of_sale, delivery, value))
