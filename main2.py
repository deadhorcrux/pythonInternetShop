from library import Library
from dataxml import Dataxml

lib1 = Library()
dat1 = Dataxml(lib1, "old.xml", "new.xml")
dat1.read()
lib1.newClient(2,"Done","don","Dondon", "Saratov", "8908778","pofj@ru","False")
dat1.write()
for k in lib1.getSalesCodes():
    print(lib1.getSalesClient(k).info())
