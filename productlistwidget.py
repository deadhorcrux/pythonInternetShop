from dbListWidget import dbListWidget

class productListWidget(dbListWidget):
    def update(self):
        self.clear()
        for a in self.getLibrary().getProductsCodes():
            self.addItem(a, self.getLibrary().getProductName(a))
        if self.getLibrary().getProductsCodes():
            self.setCurrentRow(0)
