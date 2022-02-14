from PyQt5.QtWidgets import QApplication
import sys
sys.path.insert(0, "../library")
from library import Library
from dataxml import Dataxml
from clienteditform import clientEditForm as testwidget

app = QApplication(sys.argv)
lib = Library()
data = Dataxml(lib, "old.xml")
data.read()
tw = testwidget(lib)
tw.setCurrentCode(1)
tw.show()

sys.exit(app.exec_())
