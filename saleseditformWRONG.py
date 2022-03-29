from PyQt5.QtWidgets import QLineEdit
from editform import EditForm
from salestable import salesTable

class salesEditForm(EditForm):

    def __init__(self,parent=None,library=None):
        EditForm.__init__(self,tablewidget=salesTable(library=library),parent=parent,library=library)

        self.__productEdit  = QLineEdit()
        self.__clientEdit   = QLineEdit()
        self.__datEdit      = QLineEdit()
        self.__deliveryEdit = QLineEdit()
        self.__valueEdit    = QLineEdit()

        self.addLabel(u'Product',0,0)
        self.addNewWidget(self.__productEdit,0,1)

        self.addLabel(u'Client',1,0)
        self.addNewWidget(self.__clientEdit,1,1)

        self.addLabel(u'Date of sale',2,0)
        self.addNewWidget(self.__datEdit,2,1)

        self.addLabel(u'Delivery',3,0)
        self.addNewWidget(self.__deliveryEdit,3,1)

        self.addLabel(u'Value',4,0)
        self.addNewWidget(self.__valueEdit,4,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getSalesCodes():
            self.__productEdit.setText(self.getLibrary().getSalesProduct(getCurrentCode()).info())
            self.__clientEdit.setText(self.getLibrary().getSalesClient(getCurrentCode()).info())
            self.__datEdit.setText(self.getLibrary().getSalesDate_of_sale(getCurrentCode()))
            self.__deliveryEdit.setText(self.getLibrary().getSalesDelivery(getCurrentCode()))
            self.__valueEdit.setText(self.getLibrary().getSalesValue(getCurrentCode()))

    def editClick(self):
        self.getLibrary().getSalesProduct(self.getCurrentCode(),self.__productEdit.text())
        self.getLibrary().getSalesClient(self.getCurrentCode(),self.__clientEdit.text())
        self.getLibrary().getSalesDate_of_sale(self.getCurrentCode(),self.__datEdit.text())
        self.getLibrary().getSalesDelivery(self.getCurrentCode(),self.__deliveryEdit.text())
        self.getLibrary().getSalesValue(self.getCurrentCode(),self.__valueEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getLibrary.getSalesNewCode()
        self.getLibrary().newSales(code)
        self.getLibrary().setSalesProdcut(code,self.__productEdit.text())
        self.getLibrary().setSalesClient(code,self.__clientEdit.text())
        self.getLibrary().setSalesDate_of_sale(code,self.__datEdit.text())
        self.getLibrary().setSalesDelivery(code,self.__deliveryEdit.text())
        self.getLibrary().setSalesValue(code,self.__valueEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getLibrary().removeSales(self.getCurrentCode())
        self.tableUpdate()
