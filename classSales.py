from generalList import generalList
from classClient import Client
from classProduct import Product
# from clientList import clientList
# from productList import productList

class Sales:
    def __init__(self, code, product, client, date_of_sale, delivery, value):
        self.setCode(code)
        self.setProduct(product)
        self.setClient(client)
        # self.__products = productList()
        # self.__clients = clientList()
        self.setDate_of_sale(date_of_sale)
        self.setDelivery(delivery)
        self.setValue(value)
    def setCode(self, code):
        if isinstance(code, int):
            self.__code = code
        else:
            raise Exception("code must be int")
    def getCode(self):
        return self.__code
    def setProduct(self, product):
        #if isinstance(product, Product):
        self.__product = product
        #else:
         #   raise Exception("product must be type Product")
    def getProduct(self):
        return self.__product
    def setClient(self, client):
        #if isinstance(client, Client):
        self.__client = client
        #else:
         #   raise Exception("client must be type Client")
    def getClient(self):
        return self.__client
    def setDate_of_sale(self, date_of_sale):
        if isinstance(date_of_sale, str):
            self.__date_of_sale = date_of_sale
        else:
            raise Exception("date must be string")
    def getDate_of_sale(self):
        return self.__date_of_sale
    def setDelivery(self, delivery):
        if isinstance(delivery, str):
            self.__delivery = delivery
        else:
            raise Exception("delivery must be string")
    def getDelivery(self):
        return self.__delivery
    def setValue(self, value):
        if isinstance(value, str):
            self.__value = value
        else:
            raise Exception("value must be int")
    def getValue(self):
        return self.__value
    # def appendClient(self, value):
    #     self.__clients.appendList(value)
    # def removeClient(self, code):
    #     self.__clients.removeList(code)
    # def clearClients(self):
    #     self.__clients.clear()
    # def 
    # def appendProduct(self, value):
    #     self.__products.appendList(value)
    # def removeProduct(self, code):
    #     self.__products.removeList(code)
    # def clearProducts(self):
    #     self.__products.clear()
    def info(self):
        s = "(%s) %s %s %s %s"%(self.getProduct().info(),self.getClient().info(),self.getDate_of_sale(),self.getDelivery(),self.getValue())
        return s

