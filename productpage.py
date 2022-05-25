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
            s+='<td><a href = editform?code=%s>%s</a></td>'%(c,u'edit')
            s+='<td><a href = delr?code=%s>%s</a></td></tr>'%(c,u'delete')
            r+=1
            if bg:
                bg=''
            else:
                bg=' bgcolor=silver'
        s+='</table>'
        return s
    index.exposed = True

    def productform(self, code=0, add=True):
        name,price,value='','',''
        if add:
            a='addaction'
        else:
            a='editaction?code=%s'%code
        if code in self.__lib.getProductsCodes():
            name = self.__lib.getProductName(code)
            price = self.__lib.getProductPrice(code)
            value = self.__lib.getProductValue(code)
        s='''<form action=%s method=post>
                 <table>
                     <tr><td>%s</td><td><input type = text name=name value='%s'></td></tr>
                     <tr><td>%s</td><td><input type = text name=price value='%s'></td></tr>
                     <tr><td>%s</td><td><input type = text name=value value='%s'></td></tr>
                     <tr><td><input type=submit></td><td></td></tr>
                 </table>
             </form>'''%(a,u'name',str(name),u'price',str(price),u'value',str(value))
        return s 
    def addaction(self,name, price, value):
        code = self.__lib.getProductNewCode()
        self.__lib.newProduct(code)
        self.__lib.setProductName(code, name)
        self.__lib.setProductPrice(code, price)
        self.__lib.setProductValue(code, value)
        return 'product added<br><a href=index>back</a>'
    addaction.exposed = True

    def addform(self):
        s = u'add new product<br>'
        s+= self.productform(0)
        return s
    addform.exposed = True

    def editform(self, code):
        s = u'edit product<br>'
        s+= self.productform(int(code), False)
        return s
    editform.exposed = True

    def editaction(self, code, name, price, value):
        self.__lib.setProductName(int(code), name)
        self.__lib.setProductPrice(int(code), price)
        self.__lib.setProductValue(int(code), value)
        return 'product edited<br><a href=index>back</a>'
    editaction.exposed = True

    def delr(self, code):
        self.__lib.removeProduct(int(code))
        return 'product deleted<br><a href=index>back</a>'
    delr.exposed = True



