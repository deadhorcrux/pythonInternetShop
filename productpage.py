class productpage:
    def __init__(self,library):
        self.__lib = library

    def index(self):
        s = '<a href=..>%s</a>/<a href = addform>%s</a>'%(u'back',u'add')
        s += '<table><th bgcolor = gray></th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th>'%('name','price','value')
        r=1
        bg=''
        print(self.__lib.getProductsCodes())
        for c in self.__lib.getProductsCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getProductName(c)
            s+='<td>%s</td>'%self.__lib.getProductPrice(c)
            s+='<td>%s</td>'%self.__lib.getProductValue(c)
            r+=1
            if bg:
                bg=''
            else:
                bg=' bgcolor = silver'
        s+='</table>'
        return s
    index.exposed = True



