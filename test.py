from PyQt5.QtWidgets import QApplication
import sys
sys.path.insert(0, "../library")
from library import Library
from dataxml import Dataxml
#from clienttable import clientTable as testwidget
#from salestable import salesTable as testwidget
from saleseditform import salesEditForm as testwidget

app = QApplication(sys.argv)
lib = Library()
data = Dataxml(lib, "old.xml")
data.read()
tw = testwidget(lib)
#tw.update()
tw.getCurrentCode()
tw.show()

sys.exit(app.exec_())
