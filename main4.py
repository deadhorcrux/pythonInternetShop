from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog
from PyQt5.QtGui import QIcon
import sys,os
sys.path.insert(0, "./library")
from datasql import Datasql
from dataxml import Dataxml
from library import Library
from tab import tabWidget

app = QApplication(sys.argv)

class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle(u"Shop")
        self.library = Library()
        self.dataxml = Dataxml()
        self.datasql = Datasql()

        self.tabWidget = tabWidget(self.library,self)
        self.setCentralWidget(self.tabWidget)
        self.tabWidget.update()

        self.new = QAction(QIcon(), 'New', self)
        self.new.setStatusTip('New database')
        self.new.triggered.connect(self.newAction)

        self.openxml = QAction(QIcon(), 'Open XML', self)
        self.openxml.setStatusTip('Open data from Xml')
        self.openxml.triggered.connect(self.openXmlAction)

        self.opensql = QAction(QIcon(),'Open SQL', self)
        self.opensql.setStatusTip('Open data from SQL')
        self.opensql.triggered.connect(self.openSQLAction)

        self.savexml = QAction(QIcon(), 'Save XML', self)
        self.savexml.setStatusTip('Save data to XML')
        self.savexml.triggered.connect(self.saveSQLAction)

        self.savesql = QAction(QIcon(), 'Save SQL', self)
        self.savesql.setStatusTip('Save data to SQL')
        self.savesql.triggered.connect(self.saveSQLAction)

        self.menubar = self.menuBar()
        self.menufile = self.menubar.addMenu('&File')
        self.menufile.addAction(self.new)
        self.menufile.addSeparator()
        self.menufile.addAction(self.openxml)
        self.menufile.addAction(self.opensql)
        self.menufile.addSeparator()
        self.menufile.addAction(self.savexml)
        self.menufile.addAction(self.savesql)

        self.statusBar()

    def newAction(self):
        self.library.clear()
        self.tabWidget.update()

    def openXmlAction(self):
        filename  = QFileDialog.getOpenFileName(self,u'open XML',os.getcwd(),u"*.xml")[0]
        if filename:
            self.library.clear()
            self.datasql.read(filename,self.library)
            self.tabWidget.update()
    
    def openSQLAction(self):
        filename = QFileDialog.getSaveFileName(self,u'open SQL',os.getcwd(),u"*.sqlite")[0]
        if filename:
            self.library.clear()
            self.datasql.read(filename,self.lirbary)
            self.tabWidget.update()

    def saveXmlAction(self):
        filename = QFileDialog.getSaveFileName(self,u'Save XML',os.getcwd(),u"*.xml")[0]
        if filename:
            self.dataxml.write(filename,self.library)

    def saveSQLAction(self):
        filename = QFileDialog.getSaveFileName(self,u'Save SQL',os.getcwd(),u"*.sqlite")[0]
        if filename:
            self.datasql.write(filename,self.lirbary)
mw = mainWindow()
mw.show()
sys.exit(app.exec_())
