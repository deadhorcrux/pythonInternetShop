class rowCode:
    def __init__ (self):
        self.__list = []
    def clear(self):
        self.__list = []
    def appendRowCode(self, row, code):
        self.__list.append([row, code])
    def updateRow(self, row):
        for t in self.__list:
            if t[0]>row:t[0]-=1
    def removeRow(self, row):
        for t in self.__list:
            if t[0]==row:
                self.__list.remove(t)
            self.updateRow(row)
    def removeCode(self, code):
        for t in self.__list: 
            if t[1]==code:
                self.__list.remove(t)
    def getCode(self,row):
        for t in self.__list:
            if t[0]==row:
                return t[1]
    def getCodes(self):
        return [t[1] for t in self.__list]
    def getRow(self, code):
        for t in self.__list:
            if t[1]==code:
                return t[0]

