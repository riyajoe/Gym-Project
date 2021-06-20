"An interface to implement"
from abc import ABCMeta, abstractmethod

class ISchedule(metaclass=ABCMeta):
    "An interface for an object"
    @staticmethod
    @abstractmethod
    def getSchedule(classid):
        "creates a daily schedule object"