from PyQt5.QtWidgets import QVBoxLayout,QLineEdit,QPushButton,QLabel,QSpinBox,QFileDialog
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from editform import editForm
from dbListWidget import dbListWidget
from dbComboBox import dbComboBox
from productcombo import productCombo
from clientcombo import clientCombo
from clientlistwidget import clientListWidget
from salestable import salesTable

class salesEditForm(editForm):

    def __init__(self,parent=None,library=None):

        editForm.__init__(self,tablewidget=salesTable(library=library),parent=parent,library=library)

        self.__pixlabel = QLabel()
        self.__nameEdit = QLineEdit()
        self.__imgEdit = QLineEdit()
        self.__imgButton = QPushButton(u'find')
        self.__clientListWidget = clientListWidget(library=library)
        self.__removeButton = QPushButton(u'delete')
        self.__clientCombo = clientCombo(library=library)
        self.__appendButton = QPushButton(u'add')
        self.__productCombo = productCombo(library=library)
        self.__dateSpin = QSpinBox()
        self.__dateSpin.setRange(-3000,QtCore.QDate().currentDate.year())
        self.__deliverySpin = QSpinBox()
        self.__deliverySpin.setRange(0,10000)

        self.addLabel('name',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'image',1,0)
        self.addNewWidget(self.__imgEdit,1,1)
        self.addNewWidget(self.__imgButton,1,2)
        self.addLabel(u'clients',2,0)
        self.addNewWidget(self.__clientListWidget,2,1)
        self.addNewWidget(self.__removeButton,2,2)
        self.addNewWidget(self.__clientCombo,3,1)
        self.addNewWidget(self.__appendButton,3,2)
        self.addLabel(u'product',4,0)
        self.addNewWidget(self.__productCombo,4,1)
        self.addLabel(u'date',5,0)
        self.addNewWidget(self.__dateSpin,5,1)
        self.addLabel(u'delivery',6,0)
        self.addNewWidget(self.__deliverySpin,6,1)

        self.__pixVBox = QVBoxLayout()
        self.__pixVBox.addWidget(self.__pixlabel)
        self.__pixVBox.addStretch(1)
        self.addLeftLayout(self.__pixVBox)

        self.__removeButton.clicked.connect(self.removeClient)
        self.__appendButton.clicked.connect(self.appendClient)
        self.__imgButton.clicked.connect(self.openImg)

        self.setCurrentCode()

    def openImg(self):
        filename = QFileDialog.getOpenFileName(self,'Open file', './')[0]
        if filename:
            self.__imgEdit.setText(filename)
            self.__pixlabel.setPixmap(QPixmap(filename))
    
    def update(self):
        if self.getCurrentCode() in self.getLibrary().getSalesCodes():
            self.__nameEdit.setText(self.getLibrary().getSalesProduct(self.getCurrentCode()).getName())
            self.__imgEdit.setText(self.getLibrary().getSalesClient(self.getCurrentCode()).info())
            self.__clientCombo.setCurrentRec(self.getCurrentCode())
            self.__clientListWidget.setCurrentRec(self.getCurrentCode())
            self.__productCombo.setCurrentRec(self.getCurrentCode())
            self.__deliverySpin.setValue(self.getLibrary().getSalesDelivery(self.getCurrentCode()))
            self.__dateSpin.setValue(self.getLibrary().getSalesDate_of_sale(self.getCurrentCode()))
    
    def removeProduct(self):
        code = self.clientListWidget.getCurrentCode()
        if code:
            self.__clientCombo.removeItem(self.__clientCombo.currentIndex())
            self.__clientListWidget.addItem(code,self.getLibrary().findClientByCode(code).info())

    def editClick(self):
        self.getLibrary().setSalesClient(self.getCurrentCode(), self.__nameEdit.text())
        self.getLibrary().setSalesProduct(self.getCurrentCode(), self.__imgEdit.text())
        self.getLibrary().removeClient(self.getCurrentCode())
        for c in self.__clientListWidget.getCodes():
            self.getLibrary().setSalesClient(self.getCurrentCode(),self.getLibrary().findClientByCode(c))
        self.getLibrary().setSalesProduct(self.getCurrentCode(),self.__productCombo.getCurrentCode())
        self.getLibrary().setSalesDelivery(self.getCurrentCode(),self.__deliverySpin.value())
        self.getLibrary().setSalesDate_of_sale(self.getCurrentCode(),self.__dateSpin.value())
        self.tableUpdate()

    def newClick(self):
        code = self.getLibrary().getSalesNewCode()
        self.getLibrary().newSales(code)
        self.getLibrary().setSalesClient(code,self.__nameEdit.text())
        self.getLibrary().setSalesProduct(code,self.__imgEdit.text())
        for c in self.__clientListWidget.getCodes():
            self.getLibrary().setSalesClient(code,self.getLibrary().findClientByCode(c))
        self.getLibrary().setSalesProduct(code,self.__productCombo.getCurrentCode())
        self.getLibrary().setSalesDelivery(code,self.__deliverySpin.value())
        self.getLibrary().setSalesDate_of_sale(code,self.__dateSpin.value())
        self.tableUpdate()

    def delClick(self):
        self.getLibrary().removeSales(self.getCurrentCode())
        self.tableUpdate()
