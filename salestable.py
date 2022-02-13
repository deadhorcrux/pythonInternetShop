from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class salesTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,header=[u'product',u'client',u'date of sale',u'delivery',u'value'],parent=parent)
    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getLibrary().getSalesCodes()))
        r=0
        for a in self.getLibrary().getSalesCodes():
            self.setItem(r,0,QTableWidgetItem(self.getLibrary().getSalesProduct(a).info()))
            self.setItem(r,1,QTableWidgetItem(self.getLibrary().getSalesClient(a).info()))
            self.setItem(r,2,QTableWidgetItem(self.getLibrary().getSalesDate_of_sale(a)))
            self.setItem(r,3,QTableWidgetItem(self.getLibrary().getSalesDelivery(a)))
            self.setItem(r,4,QTableWidgetItem(self.getLibrary().getSalesValue(a)))
            self.appendRowCode(r,a)
            r+=1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)
