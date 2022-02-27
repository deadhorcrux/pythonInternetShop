from dbListWidget import dbListWidget

class salesListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getLibrary.getClientCodes(self.getCurrentRec()): #needs getSalesClientCodes() 
            self.addItem(a,self.getLibrary().getClientinfo(a))
        if self.getLibrary().getClientCodes(self.getCurrentRec()):
            self.setCurrentRow(0)
