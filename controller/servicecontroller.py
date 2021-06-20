from DBcontroller.servicedbController import servicedbController

class servicecontroller:
    def __init__(self):
        self=self
        self.querylist=[]
    def getservicesByProduct(self,productlist):
        servObj=servicedbController()
        for i in productlist:
            self.querylist+=servObj.getservicedetailsByProduct(i)
        return self.querylist
    def getServiceByid(self,id):
        servObj=servicedbController()
        data=servObj.getservicedetailsByid(id)
        return data
        