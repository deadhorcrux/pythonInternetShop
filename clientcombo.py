from dbComboBox import dbComboBox

class clientCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getLibrary().getClientCodes():
            self.addItem(p,self.getLibrary().getClientName(p))
        self.setCurrentCode(self.getLibrary().getSalesClient(self.getCurrentRec()).getCode())

