from PyQt5.QtWidgets import QTableWidgetItem
from dbtablewidget import dbTableWidget

class clientTable(dbTableWidget):
    def __init__(self,library,parent=None):
        dbTableWidget.__init__(self,library=library,header=[u'soname',u'name',u'patronymic',u'address',u'phone',u'email',u'vip'],parent=parent)
    def update(self):
        self.clearContents()
        self.setRowCount(len(self.getLibrary().getClientCodes()))
        r=0
        for a in self.getLibrary().getClientCodes():
            self.setItem(r,0,QTableWidgetItem(self.getLibrary().getClientSoname(a)))
            self.setItem(r,1,QTableWidgetItem(self.getLibrary().getClientName(a)))
            self.setItem(r,2,QTableWidgetItem(self.getLibrary().getClientPatronymic(a)))
            self.setItem(r,3,QTableWidgetItem(self.getLibrary().getClientAddress(a)))
            self.setItem(r,4,QTableWidgetItem(self.getLibrary().getClientPhone(a)))
            self.setItem(r,5,QTableWidgetItem(self.getLibrary().getClientEmail(a)))
            self.setItem(r,6,QTableWidgetItem(self.getLibrary().getClientVIP(a)))
            self.appendRowCode(r,a)
            r+=1
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setCurrentCell(0,0)




