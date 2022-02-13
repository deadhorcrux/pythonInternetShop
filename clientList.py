from classClient import Client
from generalList import generalList
class clientList(generalList):
    def getSoname(self, code):
        return self.findBycode(code).getSoname()
    def getName(self, code):
        return self.findBycode(code).getName()
    def getPatronymic(self, code):
        return self.findBycode(code).getPatronymic()
    def getAddress(self, code):
        return self.findBycode(code).getAddress()
    def getPhone(self, code):
        return self.findBycode(code).getPhone()
    def getEmail(self, code):
        return self.findBycode(code).getEmail()
    def getVIP(self, code):
        return self.findBycode(code).getVIP()
    def getinfo(self, code):
        return self.findBycode(code).info()
    def infolist(self):
        s=""
        for code in self.getCodes():
            s+=self.getinfo(code)+" "
            if s:s=s[:-2]
            return s
    def setSoname(self, code, soname):
        self.findBycode(code).setSoname(soname)
    def setName(self, code, name):
        self.findBycode(code).setName(name)
    def setPatronymic(self, code, pat):
        self.findBycode(code).setPatronymic(pat)
    def setAddress(self, code, address):
        self.findBycode(code).setAddress(address)
    def setPhone(self, code, phone):
        self.findBycode(code).setPhone(phone)
    def setEmail(self, code, email):
        self.findBycode(code).setEmail(email)
    def setVIP(self, code, vip):
        self.findBycode(code).setVIP(vip)
    def newRec(self,code, soname, name, patronymic,
            address, phone, email, vip):
        self.appendList(Client(code, soname, name, patronymic,
            address, phone, email, vip))
