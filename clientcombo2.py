from dbComboBox import dbComboBox

class clientCombo(dbComboBox):
    def update(self):
        self.clear()
        for a in self.getLibrary().getClientCodes():
            if not(a in self.getLibrary().getClientCodes(self.getCurrentRec())):
                self.addItem(a,self.getLibrary().findClientByCode(a).info())
