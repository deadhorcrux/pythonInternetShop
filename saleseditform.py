from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QPushButton,QLabel,QSpinBox,QFileDialog
from PyQt5 import QtCore
from editform import EditForm
from dbListWidget import dbListWidget
from dbComboBox import dbComboBox
from productlistwidget import productListWidget
from clientlistwidget import clientListWidget
from salestable import salesTable

class salesEditForm(EditForm):

    def __init__(self,parent=None,library=None):

        EditForm.__init__(self,tablewidget=salesTable(library=library),parent=parent,library=library)

        self.__clientListWidget = clientListWidget(library=library)
        self.__productListWidget = productListWidget(library=library)
        self.__date = QLineEdit()
        self.__delivery = QLineEdit()
        self.__value = QLineEdit()

        self.addLabel('client',0,0)
        self.addNewWidget(self.__clientListWidget,0,1)
        self.addLabel(u'product',1,0) # on place where was image i put price of product
        self.addNewWidget(self.__productListWidget,1,1)
        self.addLabel(u'date',2,0)
        self.addNewWidget(self.__date,2,1)
        #self.addNewWidget(self.__removeButton,2,2)
        #self.addNewWidget(self.__appendButton,3,2)
        self.addLabel(u'value',5,0)
        self.addNewWidget(self.__value,5,1)

        #self.__removeButton.clicked.connect(self.removeClient)
        #self.__appendButton.clicked.connect(self.appendClient)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getSalesCodes():
            self.__clientListWidget.setCurrentRec(self.getCurrentCode())
            self.__productListWidget.setCurrentRec(self.getCurrentCode())
            self.__date.setText(self.getLibrary().getSalesDate_of_sale(self.getCurrentCode()))
            self.__value.setText(self.getLibrary().getSalesValue(self.getCurrentCode()))

    
    # def removeClient(self):
    #     code = self.clientListWidget.getCurrentCode()
    #     if code:
    #         self.__clientListWidget.removeSelected()
    #         self.__clientCombo.addItem(code, self.getLibrary().findClientByCode(code).info())

    # def appendClient(self):
    #     code = self.__clientCombo.getCurrentCode()
    #     if code:
    #         self.__clientCombo.removeItem(self.__clientCombo.currentIndex())
    #         self.__clientListWidget.addItem(code,self.getLibrary().findClientByCode(code).info())

    def editClick(self):
        for c in self.__productListWidget.getCodes():
            self.getLibrary().setSalesProduct(self.getCurrentCode(), self.getLibrary().findProductBycode(c))
        for c in self.__clientListWidget.getCodes():
            self.getLibrary().setSalesClient(self.getCurrentCode(),self.getLibrary().findClientBycode(c))
        self.getLibrary().setSalesDate_of_sale(self.getCurrentCode(),self.__date.text())
        self.getLibrary().setSalesValue(self.getCurrentCode(),self.__value.text())
        self.tableUpdate()

    def debug(self):
        for c in self.__clientListWidget.getCodes():
            print(self.getLibrary().findClientBycode(c).info())
        for c in self.__productListWidget.getCodes():
            print(self.getLibrary().findProductBycode(c).info())
            
    def newClick(self):
        code = self.getLibrary().getSalesNewCode()
        print(code)
        self.getLibrary().newSales(code)
        for c in self.__clientListWidget.getCodes():
            self.getLibrary().setSalesClient(code, self.getLibrary().findClientBycode(c))
        for c in self.__productListWidget.getCodes():
            self.getLibrary().setSalesProduct(code, self.getLibrary().findProductBycode(c))
        self.getLibrary().setSalesDate_of_sale(code,self.__date.text())
        self.getLibrary().setSalesValue(code,self.__value.text())
        self.tableUpdate()

    def delClick(self):
        self.getLibrary().removeSales(self.getCurrentCode())
        self.tableUpdate()
