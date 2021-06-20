from abc import ABCMeta, abstractstaticmethod

class IFactory(metaclass=ABCMeta):
    @abstractstaticmethod
    def getProduct():
        pass
    @abstractstaticmethod
    def getPrice():
        pass
    @abstractstaticmethod
    def getName():
        pass