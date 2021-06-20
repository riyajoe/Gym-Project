from interface.IService import IService
from controller.servicecontroller import servicecontroller

class Serviceblock(IService):

    def __init__(self):
        self=self


    def getService(self,sid):
        servObj=servicecontroller()
        data=servObj.getServiceByid(sid)
        return data
        