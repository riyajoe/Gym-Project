from interface.IBuilder import *
from concretebuilder.Product import *
class ProductBuilder(IBuilder):
    def __init__(self):
        self.product = Product()

    def setId(self, value):
        self.id = value
        return self
    def setName(self, value):
        self.name = value
        return self
    def setPrice(self, value):
        self.price = value
        return self
    def createBundle(self):
        return self    
    def setTrainer(self,value):
        self.trainer=value
        return self
    def setType(self,value):
        self.type=value
        return self
    def setTag(self,value):
        self.tag=value
        return self        