#from types import GenericMap

from . nexustypes import GenericMap

class Store(GenericMap):
    def __init__(self):
        GenericMap.__init__(self)


storage = Store()
