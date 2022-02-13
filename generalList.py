class generalList:
    def __init__ (self): 
        self.__list = []
    def clear(self):
        self.__list = []
    def findBycode(self, code):
        for l in self.__list:
            if l.getCode() == code:
                return l
        raise Exception("object with code %s not found" % code)
    
    def appendList(self, obj):
        self.__list.append(obj)
        
    def removeList(self, code):
        a = True
        for s in self.__list:
            if s.getCode() == code:
                self.__list.remove(s)
                a = False
        if a:
            print("object with code = %s not found" % code)
    
    def getCodes(self):
        return [s.getCode() for s in self.__list]
    
    def getNewCode(self):
        m = 0
        for c in self.getCodes():
            if c>m:m=c
            return m+1
    
    def haveContact(self, code):
        flag = False
        for l in self.__list:
            if l.getCode() == code:
                flag = True
        return flag
