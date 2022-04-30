from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QPushButton,QLabel,QSpinBox,QFileDialog
from PyQt5 import QtCore
from editform import EditForm
from dbListWidget import dbListWidget
from dbComboBox import dbComboBox
from productlistwidget import productListWidget
from clientlistwidget import clientListWidget
from salestable import salesTable
from productcombo import productCombo
from  clientcombo import clientCombo

class salesEditForm(EditForm):

    def __init__(self,parent=None,library=None):

        EditForm.__init__(self,tablewidget=salesTable(library=library),parent=parent,library=library)

        self.__clientCombo = clientCombo(library = library)
        self.__productCombo = productCombo(library = library)
        self.__date = QLineEdit()
        self.__delivery = QLineEdit()
        self.__value = QLineEdit()

        self.addLabel('client',0,0)
        self.addNewWidget(self.__clientCombo,0,1)
        self.addLabel(u'product',1,0) # on place where was image i put price of product
        self.addNewWidget(self.__productCombo,1,1)
        self.addLabel(u'date',2,0)
        self.addNewWidget(self.__date,2,1)
        self.addLabel(u'value',5,0)
        self.addNewWidget(self.__value,5,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getSalesCodes():
            self.__clientCombo.setCurrentRec(self.getCurrentCode())
            self.__productCombo.setCurrentRec(self.getCurrentCode())
            self.__date.setText(self.getLibrary().getSalesDate_of_sale(self.getCurrentCode()))
            self.__value.setText(self.getLibrary().getSalesValue(self.getCurrentCode()))

    
    def editClick(self):
        self.getLibrary().setSalesProduct(self.getCurrentCode(), self.getLibrary().findProductBycode(self.__productCombo.getCurrentCode()))
        self.getLibrary().setSalesClient(self.getCurrentCode(), self.getLibrary().findClientBycode(self.__clientCombo.getCurrentCode()))
        self.getLibrary().setSalesDate_of_sale(self.getCurrentCode(),self.__date.text())
        self.getLibrary().setSalesValue(self.getCurrentCode(),self.__value.text())
        self.tableUpdate()

    def debug(self):
        #self.getLibrary().setSalesProduct(1,None)
        pass
        
        
            
    def newClick(self):
        code = self.getLibrary().getSalesNewCode()
        self.getLibrary().newSales(code)
        self.getLibrary().setSalesClient(code,self.getLibrary().findClientBycode(self.__clientCombo.getCurrentCode()))
        self.getLibrary().setSalesProduct(code,self.getLibrary().findProductBycode(self.__productCombo.getCurrentCode()))
        self.getLibrary().setSalesDate_of_sale(code,self.__date.text())
        self.getLibrary().setSalesValue(code,self.__value.text())
        self.tableUpdate()

    def delClick(self):
        self.getLibrary().removeSales(self.getCurrentCode())
        self.tableUpdate()
