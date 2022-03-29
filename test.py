from PyQt5.QtWidgets import QApplication
import sys
sys.path.insert(0, "../library")
from library import Library
from dataxml import Dataxml
#from clienteditform import ClientEditForm as testwidget
#from producteditform import productEditForm as testwidget
#from salestable import salesTable as testwidget
from saleseditform import salesEditForm as testwidget
#from clienttable import ClientTable as testwidget

app = QApplication(sys.argv)
lib = Library()
data = Dataxml(lib, "old.xml")
data.read()
tw = testwidget(library=lib)
#tw.update() #for table
#tw.setCurrentCode(1)# was getCurrentCode() it's for someEditForm
tw.show()

sys.exit(app.exec_())
