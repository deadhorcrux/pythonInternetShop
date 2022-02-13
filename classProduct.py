class Product:
    def __init__(self, code, name, price, value):
        self.setCode(code)
        self.setName(name)
        self.setPrice(price)
        self.setValue(value)
    def setCode(self, code):
        if isinstance(code, int):
            self.__code = code
        else:
            raise Exception("code must be int")
    def getCode(self):
        return self.__code
    def setName(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("name must be string")
    def getName(self):
        return self.__name
    def setPrice(self, price):
        if isinstance(price, str):
            self.__price = price
        else:
            raise Exception("price must be int")
    def getPrice(self):
        return self.__price
    def setValue(self, value):
        if isinstance(value, str):
            self.__value = value
        else:
            raise Exception("value must be string")
    def getValue(self):
        return self.__value
    def info(self):
        s = "%s %s %s "%(self.getName(), self.getPrice(), self.getValue())
        return s
                
#obj = Product(1, "Book", 100, "sht")
#print(obj.info())
