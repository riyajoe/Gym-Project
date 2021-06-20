"An interface to implement"
from abc import ABCMeta, abstractmethod

class IService(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def getService(sid):
        "creates a service object"