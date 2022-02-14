from PyQt5.QtWidgets import QLineEdit
from editform import editForm
from clienttable import clientTable

class clientEditForm(editForm):
    def __init__(self,parent=None,library=None):
        editForm.__init__(self,tablewidget=clientTable(library=library),parent=parent,library=library)

        self.__nameEdit=QLineEdit()
        self.__sonameEdit=QLineEdit()

        self.addLabel(u'Name',0,0)
        self.addNewWidget(self.__nameEdit,0,1)
        self.addLabel(u'Soname',1,0)
        self.addNewWidget(self.__sonameEdit,1,1)

        self.setCurrentCode()

    def update(self):
        if self.getCurrentCode() in self.getLibrary().getClientCodes():
            self.__nameEdit.setText(self.getLibrary().getClientName(self.getCurrentCode()))
            self.__sonameEdit.setText(self.getLibrary().getClientSoname(self.getCurrentCode()))
    def newClick(self):
        code = self.getLibrary().getClientNewCode()
        self.getLibrary().newClient(code)
        self.getLibrary().setClientName(code,self.__nameEdit.text())
        self.getLibrary().setClientSoname(code.self.__sonameEdit.text())
        self.tableUpdate()
    def delClick(self):
        self.getLibrary().removeClient(self.getCurrentCode())
        self.tableUpdate()
