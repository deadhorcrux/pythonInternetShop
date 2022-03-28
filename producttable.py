from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class productTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,header=[u'name',u'price',u'value'],parent=parent)
    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getLibrary().getProductsCodes()))
        r=0
        for a in self.getLibrary().getProductsCodes():
            self.setItem(r,0,QTableWidgetItem(self.getLibrary().getProductName(a)))
            self.setItem(r,1,QTableWidgetItem(self.getLibrary().getProductPrice(a)))
            self.setItem(r,2,QTableWidgetItem(self.getLibrary().getProductValue(a)))
            self.appendRowCode(r,a)
            r+=1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)

