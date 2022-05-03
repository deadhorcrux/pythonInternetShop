class salespage:
    def __init__(self,library):
        self.__lib = library
    def index(self):
        s = '<a href=..>%s</a>/<a href = addform>%s</a>'%(u'back',u'add')
        s+='<table><th bgcolor = gray></th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th><th bgcolor = gray>%s</th>'%('product','client','date_of_sale','delivery','value')
        r = 1
        bg = ''
        print(self.__lib.getSalesCodes())
        for c in self.__lib.getSalesCodes():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'%self.__lib.getSalesProduct(c).getName()
            s+='<td>%s</td>'%self.__lib.getSalesClient(c).getSoname()
            s+='<td>%s</td>'%self.__lib.getSalesDate_of_sale(c)
            s+='<td>%s</td>'%self.__lib.getSalesDelivery(c)
            s+='<td>%s</td>'%self.__lib.getSalesValue(c)
            s+='<td><a href = editform?code=%s>%s</a></td>'%(c,u'edit')
            s+='<td><a href = delr?code=%s>%s</a></td></tr>'%(c,u'delete')
            r+=1
            if bg:
                bg=''
            else:
                bg=' bgcolor = silver'
        s+='</table>'
        return s
    index.exposed = True

    def clientCombo(self, code = 0):
        s = '<select name = client>'
        for c in self.__lib.getClientCodes():
            if (code in self.__lib.getSalesCodes()) and (c == self.__lib.findClientBycode(code).getCode()):
                v = ' selected'
            else:
                v = ''
            s+='<option%s value = %s>%s</option>'%(v,str(c),self.__lib.getClientName(c))
        s+='</select>'
        return s

    def productCombo(self, code = 0):
        s = '<select name = product>'
        for c in self.__lib.getProductsCodes():
            if (code in self.__lib.getSalesCodes()) and (c == self.__lib.findProductBycode(code).getCode()):
                v = ' selected'
            else:
                v = ''
            s+='<option%s value = %s>%s</option>'%(v,str(c),self.__lib.getProductName(c))
        s+='</select>'
        return s

    # def productCombo(self, code = 0):
    #     s = '<select name = product'
    #     for c in self.__lib.getProductsCodes():
    #         if (code in self.__lib.getSalesCodes()) and (c == self.__lib.findProductBycode(code).getCode()):
    #             v =' selected'
    #         else:
    #             v = ''
    #         s+='<option%s value = %s>%s</option>'%(v,str(c), self.__lib.getProductName(c))
    #     s+='</select>'
    #     return s


    def salesform(self, code = 0, add = True):
        client,product,date,delivery,val = 0,0,'','',''
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code = %s'%code
        if code in self.__lib.getSalesCodes():
            client = self.__lib.getSalesClient(code).getCode()
            product = self.__lib.getSalesProduct(code).getCode()
            date = self.__lib.getSalesDate_of_sale(code)
            delivery = self.__lib.getSalesDelivery(code)
            val  = self.__lib.getSalesValue(code)
        s='''<form action = %s method = post>
             <table>
               <tr><td>%s</td><td>%s</td></tr>
               <tr><td>%s</td><td>%s</td></tr>
               <tr><td>%s</td><td><input type = text name = date value = '%s'></td></tr>
               <tr><td>%s</td><td><input type = text name = delivery value = '%s'></td></tr>
               <tr><td>%s</td><td><input type = text name = val value = '%s'></td></tr>
               <tr><td><input type=submit></td><td></td></tr>
            </table>
            </form>'''%(a,u'client',self.clientCombo(client),u'product',self.productCombo(product),u'date',str(date),u'delivery',str(delivery),u'val',str(val))
        return s

    def addaction(self,client,product,date,delivery,val):
        code = self.__lib.getSalesNewCode()
        self.__lib.newSales(code)
        self.__lib.setSalesClient(code,int(client))
        self.__lib.setSalesProduct(code,int(product))
        self.__lib.setSalesDate_of_sale(code,date)
        self.__lib.setSalesDelivery(code,delivery)
        self.__lib.setSalesValue(code,val)
        return 'sales added<br><a href = index>back</a>'
    addaction.exposed = True

    def addform(self):
        s = u'add new sales<br>'
        s+= self.salesform(0)
        return s
    addform.exposed = True

    def editform(self,code):
        s = u'edit sales<br>'
        s+= self.salesform(int(code), False)
        s+='''%s
            <form action = addclient?code = %s method=post>
            <table>
            <tr><td>%s</td><td><input type = sumbit value = %s></td>
        '''%(u'clients',str(code),self.clientCombo(int(code)),u'add')

        s+='''%s
            <form action = addproduct?code = %s method=post>
            <table>
            <tr><td>%s</td><td><input type = sumbit value = %s></td>
        '''%(u'products',str(code),self.productCombo(int(code)),u'add')

       #  s+= self.clientList(int(code))
        return s
    editform.exposed = True

    def editaction(self,code,client,product,date,delivery,val):
        print("its a code %s"%code)
        self.__lib.setSalesClient(int(code),client)
        self.__lib.setSalesProduct(int(code),product)
        self.__lib.setSalesDate_of_sale(int(code),date)
        self.__lib.setSalesDelivery(int(code),delivery)
        self.__lib.setSalesValue(int(code),val)
        return 'sales edited<br><a href = index>back</a>'

    editaction.exposed = True

    def delr(self,code):
        self.__lib.removeSales(int(code))
        return 'sales deleted<br><a href = index>back</a>'

    delr.exposed = True
