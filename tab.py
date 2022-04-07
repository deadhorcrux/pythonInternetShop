from PyQt5.QtWidgets import QTabWidget
import sys
import os
from saleseditform import salesEditForm
from clienteditform import clientEditForm
from producteditform import productEditForm

class tabWidget(QTabWidget):
    def __init__(self,library,parent = None):
        QTabWidget.__init__(self,parent)
        self.__salesEditForm = salesEditForm(library = library)
        self.addTab(self.__salesEditForm,u"sales")
        
        self.__clientEditForm = clientEditForm(library = library)
        self.addTab(self.__clientEditForm,u"clients")

        self.__productEditForm = productEditForm(library = library)
        self.addTab(self.__productEditForm,u"products")

    def update(self):
        self.__productEditForm.tableUpdate()
        self.__clientEditForm.tableUpdate()
        self.__salesEditForm.tableUpdate()

