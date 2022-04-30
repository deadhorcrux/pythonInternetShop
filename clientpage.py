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
