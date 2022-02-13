class Data:
    def __init__(self, lib=None, inp='', out=''):
        self.setLib(lib)
        self.setInp(inp)
        self.setOut(out)
    def setLib(self, lib):
        self.__lib = lib
    def setInp(self, inp):
        self.__inp = inp
    def setOut(self, out):
        self.__out = out
    def getLib(self):
        return self.__lib
    def getInp(self):
        return self.__inp
    def getOut(self):
        return self.__out

    def readFile(self, filename):
        self.setInp(filename)
        self.read()
    def writeFile(self, filename):
        self.setOut(filename)
        self.write()
    def read(self):
        pass
    def write(self):
        pass

    
