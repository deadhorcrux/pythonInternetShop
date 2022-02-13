from PyQt5.QtWidgets import QApplication
import sys
sys.path.insert(0, "../library")
from library import Library
from dataxml import Dataxml
from salestable import salesTable

app = QApplication(sys.argv)
lib = Library()
data = Dataxml(lib, "old.xml")
data.read()
tw1 = salesTable(lib)
tw1.update()
tw1.show()

sys.exit(app.exec_())
