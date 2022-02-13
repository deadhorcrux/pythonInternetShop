from clientList import clientList
from salesList import salesList
from productList import productList

class  Library:
    def __init__(self):
        self.__clients = clientList()
        self.__sales = salesList()
        self.__products = productList()
    def removeClient(self, code):
        for i in self.__clients.getCodes():
            if i == code:
                if(self.__sales.haveContact(code)):
                    print("client with code %s contact with sales - %s"%(code,self.findSalesBycode(code).info()))
                else:
                    self.__clients.removeList(code)
    def removeSales(self, code):
        self.__sales.removeList(code)
    def removeProduct(self, code):
        for i in self.__products.getCodes():
            if i == code:
                if(self.__sales.haveContact(code)):
                    print("product with code %s contact with client - %s"%(code,self.findClientBycode(code).info()))
                else:
                    self.__products.removeList(code)

    def clear(self):
        self.__clients.clear()
        self.__sales.clear()
        self.__products.clear()
    
    def newClient(self, code=0, soname='', name='',
            patronymic='', address='', phone='', email='', vip=''):
        self.__clients.newRec(code, soname, name,
                patronymic, address, phone, email, vip)        
    def findClientBycode(self, code):
        return self.__clients.findBycode(code)
    def getClientCodes(self):
        return self.__clients.getCodes()
    def getClientNewCode(self):
        return self.__clients.getNewCode()
    def getClientName(self, code):
        return self.__clients.findBycode(code).getName()
    def getClientSoname(self, code):
        return self.__clients.findBycode(code).getSoname()
    def getClientPatronymic(self,code):
        return self.__clients.findBycode(code).getPatronymic()
    def getClientAddress(self, code):
        return self.__clients.findBycode(code).getAddress()
    def getClientPhone(self, code):
        return self.__clients.findBycode(code).getPhone()
    def getClientEmail(self, code):
        return self.__clients.findBycode(code).getEmail()
    def getClientVIP(self, code):
        return self.__clients.findBycode(code).getVIP()
    def getClientInfo(self, code):
        return self.__clients.findBycode(code).info()
    def setClientName(self, code, name):
       self.__clients.setName(code, name)
    def setClientSoname(self, code, soname):
        self.__clients.setSoname(code, soname)
    def setClientPatronymic(self, code, patronymic):
        self.__clients.setPatronymic(code, patronymic)
    def setClientAddress(self, code, address):
        self.__clients.setAddress(code, address)
    def setClientPhone(self, code, phone):
        self.__clients.setPhone(code, phone)
    def setClientEmail(self, code, email):
        self.__clients.setEmail(code, email)
    def setClientVip(self, code, vip):
        self.__clients.setVIP(code, vip)

    def newProduct(self, code=0, name='', price=0, value=''):
        self.__products.newRec(code, name, price, value)
    def findProductBycode(self, code):
        return self.__products.findBycode(code)
    def getProductNewCode(self):
        return self.__products.getNewCode()
    def getProductsCodes(self):
        return self.__products.getCodes()
    def getProductName(self, code):
        return self.__products.getName(code)
    def getProductPrice(self, code):
        return self.__products.getPrice(code)
    def getProductValue(self, code):
        return self.__products.getValue(code)
    def getProductInfo(self,code):
        return self.__products.findBycode(code).info()
    def setProductName(self, code, name):
        self.__products.findBycode(code).setName(name)
    def setProductPrice(self, code, price):
        self.__products.findBycode(code).setPrice(price)
    def setProductValue(self, code, value):
        self.__products.findBycode(code).setValue(value)

    def newSales(self, code=0, product=None, client=None, date_of_sale='', delivery='', value=''):
        self.__sales.newRec(code, product, client, date_of_sale, delivery, value)
    def findSalesBycode(self, code):
        return self.__sales.findBycode(code)
    def getSalesNewCode(self):
        return self.__sales.getNewCode()
    def getSalesCodes(self):
        return self.__sales.getCodes()
    def getSalesDate_of_sale(self, code):
        return self.__sales.getDate_of_sale(code)
    def getSalesProduct(self, code):
        return self.__sales.getProduct(code)
    def getSalesClient(self, code):
        return self.__sales.getClient(code)
    def getSalesValue(self, code):
        return self.__sales.getValue(code)
    def getSalesDelivery(self, code):
        return self.__sales.getDelivery(code)
    def getSalesInfo(self, code):
        return self.__sales.findBycode(code).info()
    def setSalseDate_of_sale(self, code, date_of_sale):
        self.__sales.findBycode(code).setDate_of_sale(date_of_sale)
    def setSalesDelivery(self, code, delivery):
        self.__sales.findBycode(code).setDelivery(delivery)
    def setSalesValue(self, code, value):
        self.__sales.findBycode(code).setValue(value)
    def setSalesProduct(self, code, product):
        self.__sales.findBycode(code).setProduct(product)
    def setSalesClient(self, code, client):
        self.__sales.findBycode(code).setClient(client)
    
