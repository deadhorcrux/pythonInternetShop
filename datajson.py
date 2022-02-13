import json
from data import Data

class DataJson(Data):
    def read(self):
        with open(self.getInp(), "r") as read_file:
            data=json.load(read_file)
        for k in data.keys():
            if k == "clients":
                for a in data[k]:
                    code,soname,name,patronymic,address,phone,email,vip=0,"","","","","","",""
                    for ak in a.keys():
                        if ak == "code": code = a[ak]
                        if ak == "soname": soname = a[ak]
                        if ak == "name": name = a[ak]
                        if ak == "patronymic": patronymic = a[ak]
                        if ak == "address": address = a[ak]
                        if ak == "phone": phone = a[ak]
                        if ak == "email": email = a[ak]
                        if ak == "vip": vip = a[ak]
                    self.getLib().newClient(code,soname,name,patronymic,address,phone,email,vip)
            if k == "products":
                for a in data[k]:
                    code,name,price,value=0,"","",""
                    for ak in a.keys():
                        if ak == "code": code = a[ak]
                        if ak == "name": name = a[ak]
                        if ak == "price": price = a[ak]
                        if ak == "value": value = a[ak]
                    self.getLib().newProduct(code,name,price,value)
            if k == "sales":
                for a in data[k]:
                    code,product,client,date_of_sale,delivery,value=0,"","","","",""
                    for ak in a.keys():
                        if ak == "code": code = a[ak]
                        if ak == "product": product = self.getLib().findProductBycode(a[ak])
                        if ak == "client": client = self.getLib().findClientBycode(a[ak])
                        if ak == "date_of_sale": date_of_sale = a[ak]
                        if ak == "delivery": delivery = a[ak]
                        if ak == "value": value = a[ak]
                    self.getLib().newSales(code,product,client,date_of_sale,delivery,value)
    def write(self):
        data = {"clients": [], "products": [], "sales": []}
        for c in self.getLib().getClientCodes():
            a={}
            a["code"] = c
            a["soname"] = self.getLib().getClientSoname(c)
            a["name"] = self.getLib().getClientName(c)
            a["patronymic"] = self.getLib().getClientPatronymic(c)
            a["address"] = self.getLib().getClientAddress(c)
            a["phone"] = self.getLib().getClientPhone(c)
            a["email"] = self.getLib().getClientEmail(c)
            a["vip"] = self.getLib().getClientVIP(c)
            data["clients"].append(a)
        for c in self.getLib().getProductsCodes():
            a = {}
            a["code"] = c
            a["name"] = self.getLib().getProductName(c)
            a["price"] = self.getLib().getProductPrice(c)
            a["value"] = self.getLib().getProductValue(c)
            data["products"].append(a)
        for c in self.getLib().getSalesCodes():
            a = {}
            a["code"] = c
            a["product"] = self.getLib().findProductBycode(c).getCode()
            a["client"] = self.getLib().findClientBycode(c).getCode()
            a["date_of_sale"] = self.getLib().getSalesDate_of_sale(c)
            a["delivery"] = self.getLib().getSalesDelivery(c)
            a["value"] = self.getLib().getSalesValue(c)
            data["sales"].append(a)
        with open(self.getOut(), "w") as write_file:
            json.dump(data, write_file, indent=4, separators=(',', ': '), ensure_ascii=False)

