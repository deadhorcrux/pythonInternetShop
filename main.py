from classClient import Client
from classProduct import Product
from classSales import Sales
from generalList import generalList
from clientList import clientList
from salesList import salesList
from productList import productList
from data import Data
from library import Library


if __name__ == "__main__":
    lib = Library()
    client = Client(1, "Killer", "Sanchelo", "Mamkin",
                    "Saratov","9371439900","pof@mail.ru","False")
    product = Product(1, "King", "200", "sht")
    lib.newClient(1, "Killer", "Sanchelo", "Mamkin",
            "Saratov","9371439900","pof@mail.ru","False")
    lib.newProduct(1, "King", "200", "sht")
    lib.newSales(1, product, client, "12", "1", "1")
    lib.newClient(2,"Done","don","Dondon", "Saratov", "8908778","pofj@ru","False")
    # lib.removeClient(2)
    # for i in lib.getClientCodes():
    #     print(lib.findClientBycode(i).info())
    lib.removeSales(1)
