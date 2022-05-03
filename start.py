import cherrypy
import sys
sys.path.insert(0, "./library")
from library import Library 
from dataxml import Dataxml 
from clientpage import clientpage
from productpage import productpage
from salespage import salespage

class start:
    def __init__(self):
        self.__lib = Library()
        self.__dataxml = Dataxml(self.__lib, "old.xml")
        self.__dataxml.read()
        self.clientpage = clientpage(self.__lib)
        self.productpage = productpage(self.__lib)
        self.salespage = salespage(self.__lib)

    def index(self):
        return """
    <a href=clientpage\>client</a><br>
    <a href=productpage\>product</a><br>
    <a href=salespage\>sales</a><br>
    """
    index.exposed = True

root = start()

cherrypy.config.update({
    'log.screen': True,
    })

cherrypy.tree.mount(root)

if __name__ == "__main__":
    cherrypy.engine.start()
    cherrypy.engine.block()


