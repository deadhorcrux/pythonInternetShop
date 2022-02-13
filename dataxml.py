import os
import xml.dom.minidom
from data import Data

class Dataxml(Data):
    def read(self):
        dom = xml.dom.minidom.parse(self.getInp())
        dom.normalize()
        
        for node in dom.childNodes[0].childNodes:
            if (node.nodeType==node.ELEMENT_NODE) and (node.nodeName=='client'):
                
                code,soname,name,patronymic,address,phone,email,vip=0,"","","","","","",False
                
                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="soname":soname=t[1]
                    if t[0]=="name":name=t[1]
                    if t[0]=="patronymic":patronymic=t[1]
                    if t[0]=="address":address=t[1]
                    if t[0]=="phone":phone=t[1]
                    if t[0]=="email":email=t[1]
                    if t[0]=="vip":vip=t[1]
                self.getLib().newClient(code,soname,name,patronymic,address,phone,email,vip)
                
            if (node.nodeType==node.ELEMENT_NODE) and (node.nodeName=='product'):
                
                code,name,price,value=0,"",0,0

                for t in node.attributes.items():
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="name":name=t[1]
                    if t[0]=="price":price=t[1]
                    if t[0]=="value":value=t[1]
                self.getLib().newProduct(code, name, price, value)
                
            if (node.nodeType==node.ELEMENT_NODE) and (node.nodeName=='sales'):
                code,product,client,date_of_sale,delivery,value=0,None,None,"","",0

                for t in node.attributes.items():
                    
                    if t[0]=="code":code=int(t[1])
                    if t[0]=="product":product=self.getLib().findProductBycode(int(t[1]))
                    if t[0]=="client":client=self.getLib().findClientBycode(int(t[1]))
                    if t[0]=="date_of_sale":date_of_sale=t[1]
                    if t[0]=="delivery":delivery=t[1]
                    if t[0]=="value":value=t[1]
                self.getLib().newSales(code,product,client,date_of_sale,delivery,value)
                
    def write(self):
        dom = xml.dom.minidom.Document()
        root = dom.createElement("library")
        dom.appendChild(root)
        
        for c in self.getLib().getClientCodes():
            cl = dom.createElement("client")
            cl.setAttribute('code',str(c))
            cl.setAttribute('soname',self.getLib().getClientSoname(c))
            cl.setAttribute('name',self.getLib().getClientName(c))
            cl.setAttribute('patronymic',self.getLib().getClientPatronymic(c))
            cl.setAttribute('address',self.getLib().getClientAddress(c))
            cl.setAttribute('phone',self.getLib().getClientPhone(c))
            cl.setAttribute('email',self.getLib().getClientEmail(c))
            cl.setAttribute('vip',self.getLib().getClientVIP(c))
            root.appendChild(cl)
            
        for c in self.getLib().getProductsCodes():
            pr = dom.createElement("product")
            pr.setAttribute('code',str(c))
            pr.setAttribute('name',self.getLib().getProductName(c))
            pr.setAttribute('price',self.getLib().getProductPrice(c))
            pr.setAttribute('value',self.getLib().getProductValue(c))
            root.appendChild(pr)
            
        for c in self.getLib().getSalesCodes():
            sal  = dom.createElement("sales")
            sal.setAttribute('code',str(c))
            sal.setAttribute('product',str(self.getLib().getSalesProduct(c).getCode()))
            sal.setAttribute('client',str(self.getLib().getSalesClient(c).getCode()))
            sal.setAttribute('date_of_sale',self.getLib().getSalesDate_of_sale(c))
            sal.setAttribute('delivery',self.getLib().getSalesDelivery(c))
            sal.setAttribute('value',self.getLib().getSalesValue(c))
            root.appendChild(sal)
        
        f = open(self.getOut(),"w")
        f.write(dom.toprettyxml())
