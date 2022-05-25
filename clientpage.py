class clientpage:
    def __init__(self,library):
        self.__lib = library

    def index(self):
        s = '<a href=..>%s</a>/<a href = addform>%s</a>'%(u'back',u'add')
        s += '<table><th bgcolor = gray></th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th>'%('soname','name','patronymic','address','phone','email')
        r = 1
        bg = ''
        print(self.__lib.getClientCodes())
        for c in self.__lib.getClientCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getClientSoname(c)
            s+='<td>%s</td>'%self.__lib.getClientName(c)
            s+='<td>%s</td>'%self.__lib.getClientPatronymic(c)
            s+='<td>%s</td>'%self.__lib.getClientAddress(c)
            s+='<td>%s</td>'%self.__lib.getClientPhone(c)
            s+='<td>%s</td>'%self.__lib.getClientEmail(c)
            s+="<td><a href = editform?code=%s>%s</a></td>"%(c,u'edit')
            s+='<td><a href = delr?code=%s>%s</a></td></tr>'%(c,u'delete')
            r += 1
            if bg:
                bg=''
            else:
                bg=' bgcolor = silver'
        s+='</table>'
        return s
    index.exposed = True

    def clientform(self, code=0, add=True):
        soname,name,pat,address,phone,email = '','','','','',''
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s'%code
        if code in self.__lib.getClientCodes():
            soname = self.__lib.getClientSoname(code)
            name = self.__lib.getClientName(code)
            pat = self.__lib.getClientPatronymic(code)
            address = self.__lib.getClientAddress(code)
            phone = self.__lib.getClientPhone(code)
            email = self.__lib.getClientEmail(code)
        s='''<form action=%s method=post>
             <table>
             <tr><td>%s</td><td><input type = text name = soname value = '%s'></td></tr>
             <tr><td>%s</td><td><input type = text name = name value = '%s'></td></tr>
             <tr><td>%s</td><td><input type = text name = pat value = '%s'></td></tr>
             <tr><td>%s</td><td><input type = text name = address value = '%s'></td></tr>
             <tr><td>%s</td><td><input type = text name = phone value = '%s'></td></tr>
             <tr><td>%s</td><td><input type = text name = email value = '%s'></td></tr>
             <tr><td><input type=submit></td><td></td></tr>
             </table>
             </form>'''%(a,u'soname',str(soname),u'name',str(name),u'patronymic',str(pat),u'address',str(address),u'phone',str(phone),u'email',str(email))
        return s
    def addaction(self,soname,name,pat,address,phone,email):
        code = self.__lib.getClientNewCode()
        self.__lib.newClient(code)
        self.__lib.setClientSoname(code,soname)
        self.__lib.setClientName(code,name)
        self.__lib.setClientPatronymic(code,pat)
        self.__lib.setClientAddress(code,address)
        self.__lib.setClientPhone(code,phone)
        self.__lib.setClientEmail(code,email)
        return 'client added<br><a href=index>back</a>'
    addaction.exposed = True

    def addform(self):
        s = u'add new client<br>'
        s+= self.clientform(0)
        return s
    addform.exposed = True

    def editform(self,code):
        s=u'edit client<br>'
        s+= self.clientform(int(code),False)
        return s
    editform.exposed = True

    def editaction(self,code,soname,name,pat,address,phone,email):
        self.__lib.setClientSoname(int(code),soname)
        self.__lib.setClientName(int(code),name)
        self.__lib.setClientPatronymic(int(code),pat)
        self.__lib.setClientAddress(int(code),address)
        self.__lib.setClientPhone(int(code),phone)
        self.__lib.setClientEmail(int(code),email)
        return 'client edited<br><a href=index>back</a>'
    editaction.exposed = True

    def delr(self,code):
        self.__lib.removeClient(int(code))
        return 'client deleted<br><a href=index>back</a>'
    delr.exposed = True
