from library import Library
from dataxml import Dataxml 

lib1 = Library()
dat1 = Dataxml(lib1, "old.xml", "delete.xml")
dat1.read()
lib1.newClient(2,"Done","don","Dondon", "Saratov", "8908778","pofj@ru","False")
lib1.newProduct(2,"kin", "200", "litr")
lib1.removeClient(2)
#lib1.removeProduct(1)
lib1.removeSales(1)
dat1.write()
dat_d = Dataxml(lib1, "delete.xml", "after.xml")
dat_d.read()
lib1.clear()
dat_d.write()
 
