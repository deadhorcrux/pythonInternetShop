from library import Library
from datajson import DataJson

lib1 = Library()
dat1 = DataJson(lib1, 'old.json', 'new.json')
dat1.read()
dat1.write()
for k in lib1.getSalesCodes():
    print(lib1.getSalesClient(k).info())
