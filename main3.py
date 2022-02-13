from library import Library
from datasql import Datasql
from dataxml import Dataxml
import os

lib1 = Library()
lib2 = Library()

dxml1 = Dataxml(lib1, 'old.xml', 'new.xml')
dxml2 = Dataxml(lib2, 'old.xml', 'new.xml')

dsql1 = Datasql(lib1, 'new.sqlite', 'new.sqlite')
dsql2 = Datasql(lib2, 'new.sqlite', 'new.sqlite')

dxml1.read()

if os.path.isfile(dsql1.getOut()):os.remove(dsql1.getOut())
dsql1.write()
dsql2.read()
dxml2.write()
