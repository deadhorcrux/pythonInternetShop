from PyQt5.QtWidgets import QLineEdit
from editform import EditForm
from producttable import productTable

class productEditForm(EditForm):

    def __init__(self,parent=None,library=None):
        EditForm.__init__(self,tablewidget=productTable(library=library),parent=parent,library=library)

        self.__nameEdit  = QLineEdit()
        self.__priceEdit = QLineEdit()
        self.__valueEdit = QLineEdit()

        self.addLabel(u'Name',0,0)
        self.addNewWidget(self.__nameEdit,0,1)

        self.addLabel(u'Price',1,0)
        self.addNewWidget(self.__priceEdit,1,1)

        self.addLabel(u'Value',2,0)
        self.addNewWidget(self.__valueEdit,2,1)

        self.setCurrentCode()
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getProductsCodes():
            self.__nameEdit.setText(self.getLibrary().getProductName(self.getCurrentCode()))
            self.__priceEdit.setText(self.getLibrary().getProductPrice(self.getCurrentCode()))
            self.__valueEdit.setText(self.getLibrary().getProductPrice(self.getCurrentCode()))
    
    def editClick(self): 
        self.getLibrary().setProductName(self.getCurrentCode(),self.__nameEdit.text())
        self.getLibrary().setProductPrice(self.getCurrentCode(),self.__priceEdit.text())
        self.getLibrary().setProductValue(self.getCurrentCode(),self.__valueEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getLibrary.getProductNewCode()
        self.getLibrary().newProduct(code)
        self.getLibrary().setProductName(code,self.__nameEdit.text())
        self.getLibrary().setProductPrice(code,self.__priceEdit.text())
        self.getLibrary().setProductValue(code,self.__valueEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getLibrary().removeProduct(self.getCurrentCode())
        self.tableUpdate()
