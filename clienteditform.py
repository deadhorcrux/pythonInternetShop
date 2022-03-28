from PyQt5.QtWidgets import QLineEdit
from editform import EditForm
from clienttable import ClientTable

class ClientEditForm(EditForm):
    def __init__(self,parent=None,library=None):
        EditForm.__init__(self,tablewidget=ClientTable(library=library),parent=parent,library=library)

        self.__nameEdit       = QLineEdit()
        self.__sonameEdit     = QLineEdit()
        self.__patronymicEdit = QLineEdit()
        self.__addressEdit    = QLineEdit()
        self.__phoneEdit      = QLineEdit()
        self.__emailEdit      = QLineEdit()
        self.__vipEdit        = QLineEdit()

        self.addLabel(u'Name',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        
        self.addLabel(u'Soname',1,0)
        self.addNewWidget(self.__sonameEdit,1,1)
        
        self.addLabel(u'Patronymic',2,0)
        self.addNewWidget(self.__patronymicEdit,2,1)
        
        self.addLabel(u'Address',3,0)
        self.addNewWidget(self.__addressEdit,3,1)
        
        self.addLabel(u'Phone',4,0)
        self.addNewWidget(self.__phoneEdit,4,1)
        
        self.addLabel('Email',5,0)
        self.addNewWidget(self.__emailEdit,5,1)
        
        self.addLabel(u'VIP',6,0)
        self.addNewWidget(self.__vipEdit,6,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getClientCodes():
            self.__nameEdit.setText(self.getLibrary().getClientName(self.getCurrentCode()))
            self.__sonameEdit.setText(self.getLibrary().getClientSoname(self.getCurrentCode()))
            self.__patronymicEdit.setText(self.getLibrary().getClientPatronymic(self.getCurrentCode()))
            self.__addressEdit.setText(self.getLibrary().getClientAddress(self.getCurrentCode()))
            self.__phoneEdit.setText(self.getLibrary().getClientPhone(self.getCurrentCode()))
            self.__emailEdit.setText(self.getLibrary().getClientEmail(self.getCurrentCode()))
            self.__vipEdit.setText(self.getLibrary().getClientVIP(self.getCurrentCode()))

    def editClick(self):
        self.getLibrary().setClientName(self.getCurrentCode(),self.__nameEdit.text())
        self.getLibrary().setClientSoname(self.getCurrentCode(),self.__sonameEdit.text())
        self.getLibrary().setClientPatronymic(self.getCurrentCode(),self.__patronymicEdit.text())
        self.getLibrary().setClientAddress(self.getCurrentCode(),self.__addressEdit.text())
        self.getLibrary().setClientPhone(self.getCurrentCode(),self.__phoneEdit.text())
        self.getLibrary().setClientEmail(self.getCurrentCode(),self.__emailEdit.text())
        self.getLibrary().setClientVip(self.getCurrentCode(),self.__vipEdit.text())
        self.tableUpdate()

    def newClick(self):
        code = self.getLibrary().getClientNewCode()
        self.getLibrary().newClient(code)
        self.getLibrary().setClientName(code,self.__nameEdit.text())
        self.getLibrary().setClientSoname(code,self.__sonameEdit.text())
        self.getLibrary().setClientPatronymic(code,self.__patronymicEdit.text())
        self.getLibrary().setClientAddress(code,self.__addressEdit.text())
        self.getLibrary().setClientPhone(code,self.__phoneEdit.text())
        self.getLibrary().setClientEmail(code,self.__emailEdit.text())
        self.getLibrary().setClientVip(code,self.__vipEdit.text())
        self.tableUpdate()

    def delClick(self):
        self.getLibrary().removeClient(self.getCurrentCode())
        self.tableUpdate()
