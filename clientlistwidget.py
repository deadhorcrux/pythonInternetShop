from dbListWidget import dbListWidget

class clientListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getLibrary().getClientCodes(self.getCurrentRec()):
            self.addItem(a,self.getLibrary().findClientByCode(a).info())
        if self.getLibrary().getClientCodes(self.getCurrentRec()):
            self.setCurrentRow(0)
