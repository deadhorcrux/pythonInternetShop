from dbComboBox import dbComboBox

class productCombo(dbComboBox):
    def update(self):
        self.clear()
        for p in self.getLibrary().getProductsCodes():
            self.addItem(p,self.getLibrary().getProductName(p))
        self.setCurrentCode(self.getLibrary().getSalesProduct(self.getCurrentRec()).getCode())
