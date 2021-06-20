from abc import ABCMeta,abstractstaticmethod
class IBuilder(metaclass=ABCMeta):
    "The interface for bundle creation"
    @abstractstaticmethod
    def setId(self,value):
        "set id parameter for bundle"
        pass
    @abstractstaticmethod
    def setName(self,value):
        "set name parameter for bundle"   
        pass
    @abstractstaticmethod
    def setPrice(self,value):
        "set price parameter for bundle"
        pass
    @abstractstaticmethod
    def createBundle(self):
        "return object"
        pass
    @abstractstaticmethod
    def setType(self):
        pass
    @abstractstaticmethod
    def setTrainer(self):
        pass
    @abstractstaticmethod
    def setTag(self):
        pass
           