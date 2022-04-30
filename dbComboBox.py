from libwidget import LibWidget
from PyQt5.QtWidgets import QComboBox
from rowCode import rowCode

class dbComboBox(QComboBox,LibWidget):
    def __init__(self,parent=None,library=None):
        QComboBox.__init__(self,parent)
        LibWidget.__init__(self,library)
        self.__rowCode = rowCode()
        self.setSizeAdjustPolicy(self.AdjustToContents)

    def clear(self):
        self.__rowCode.clear()
        QComboBox.clear(self)

    def addItem(self,code,text):
        self.__rowCode.appendRowCode(self.count(),code)
        QComboBox.addItem(self,text)

    def removeItem(self,index):
        self.__rowCode.removeRow(index)
        QComboBox.removeItem(self,index)
    
    def getCurrentCode(self):
        return self.__rowCode.getCode(self.currentIndex())
    def setCurrentCode(self,code):
        #print(self.__rowCode.getRow(code),code)
        if self.__rowCode.getRow(code):
            self.setCurrentIndex(self.__rowCode.getRow(code))
    def setCurrentRec(self,value):
        self.__currentRec = value
        self.update()
    def getCurrentRec(self):
        return self.__currentRec
    def update(self):
        pass
