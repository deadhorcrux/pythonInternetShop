from dbListWidget import dbListWidget

class clientListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getLibrary().getClientCodes():
            self.addItem(a,self.getLibrary().getClientSoname(a))
        if self.getLibrary().getClientCodes():
            self.setCurrentRow(0)
