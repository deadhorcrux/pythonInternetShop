import os
import sqlite3 as db
from data import Data

emptydb = """
PRAGMA foreign_keys = ON;
create table client
(code integer primary key,
 soname text,
 name text,
 patronymic text,
 address text,
 email text,
 phone text,
 vip text);

create table product
(code integer primary key,
 name text,
 price text,
 value text);

create table sales
(code integer primary key autoincrement,
 product integer references product(code) on update cascade on delete set null,
 client integer references client(code) on update cascade on delete set null,
 date_of_sale text,
 delivery text,
 value text);
"""

class Datasql(Data):
    def read(self):
        conn = db.connect(self.getInp())
        curs = conn.cursor()
        curs.execute('select code, soname, name, patronymic, address, email, phone, vip from client')
        data = curs.fetchall()
        for r in data:self.getLib().newClient(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
        curs.execute('select code, name, price, value from product')
        data = curs.fetchall()
        for r in data:self.getLib().newProduct(r[0], r[1], r[2], r[3])
        curs.execute('select code, product, client, date_of_sale, delivery, value from sales')
        data = curs.fetchall()
        for r in data:self.getLib().newSales(r[0], self.getLib().findProductBycode(int(r[1])), self.getLib().findClientBycode(int(r[2])), r[3], r[4], r[5])
        conn.close()
    def write(self):
        conn = db.connect(self.getOut())
        curs = conn.cursor()
        curs.executescript(emptydb)
        for c in self.getLib().getClientCodes():
            curs.execute("insert into client(code,soname,name,patronymic,address,email,phone,vip) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(
                str(c),
                self.getLib().getClientSoname(c),
                self.getLib().getClientName(c),
                self.getLib().getClientPatronymic(c),
                self.getLib().getClientAddress(c),
                self.getLib().getClientEmail(c),
                self.getLib().getClientPhone(c),
                self.getLib().getClientVIP(c)))
        for c in self.getLib().getProductsCodes():
            curs.execute("insert into product(code,name,price,value) values('%s','%s','%s','%s')"%(
                str(c),
                self.getLib().getProductName(c),
                self.getLib().getProductPrice(c),
                self.getLib().getProductValue(c)))
        for c in self.getLib().getSalesCodes():
            curs.execute("insert into sales(code,product,client,date_of_sale,delivery,value) values('%s','%s','%s','%s','%s','%s')"%(
                str(c),
                str(self.getLib().findProductBycode(int(c)).getCode()),
                str(self.getLib().findClientBycode(int(c)).getCode()),
                self.getLib().getSalesDate_of_sale(c),
                self.getLib().getSalesDelivery(c),
                self.getLib().getSalesValue(c)))
        conn.commit()
        conn.close()
