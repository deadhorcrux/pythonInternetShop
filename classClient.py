class Client:
    def __init__(self, code, soname, name, patronymic,
            address, phone, email, vip):
        self.setCode(code)
        self.setSoname(soname)
        self.setName(name)
        self.setPatronymic(patronymic)
        self.setAddress(address)
        self.setPhone(phone)
        self.setEmail(email)
        self.setVIP(vip)
    def setCode(self, code):
        if isinstance(code, int):
            self.__code = code
        else:
            raise Exception("code must be int")
    def getCode(self):
        return self.__code
    def setSoname(self, soname):
        if isinstance(soname, str):
            self.__soname = soname
        else:
            raise Exception("soname must be string")
    def getSoname(self):
        return self.__soname
    def setName(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("name must be string")
    def getName(self):
        return self.__name
    def setPatronymic(self, patronymic):
        if isinstance(patronymic, str):
            self.__patronymic = patronymic
        else:
            raise Exception("patronymic must be string")
    def getPatronymic(self):
        return self.__patronymic
    def setAddress(self, address):
        if isinstance(address, str):
            self.__address = address
        else:
            raise Exception("address must be string")
    def getAddress(self):
        return self.__address
    def setPhone(self, phone):
        if isinstance(phone, str):
            self.__phone = phone
        else:
            raise Exception("phone must be int")
    def getPhone(self):
        return self.__phone
    def setEmail(self, email):
        if isinstance(email, str):
            self.__email = email
        else:
            raise Exception("email must be string")
    def getEmail(self):
        return self.__email
    def setVIP(self, vip):
        if isinstance(vip, str):
            self.__vip = vip
        else:
            raise Exception("true or false")
    def getVIP(self):
        return self.__vip

    def info(self):
        s = "%s %s %s %s %s %s %s"%(self.getSoname(),self.getName(),self.getPatronymic(),self.getAddress(),self.getPhone(),self.getEmail(),self.getVIP())
        return s

