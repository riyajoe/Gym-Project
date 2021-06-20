
from models.Service import *
from app import db

class servicedbController:
    def __init__(self):
        self=self
    def addService(self,ServObj,pid):
        db.create_all()
        Serv=Service(sid=ServObj.id,pid=pid,sname=ServObj.name,sprice=ServObj.price,trainer=ServObj.trainer)
        db.session.add(Serv)
        db.session.commit()

    def getservicedetailsByProduct(self,productlist):
        return db.session.query(Service).filter(Service.pid==productlist).all()

    def getservicedetailsByid(self,id):
        return db.session.query(Service).filter(Service.sid==id).first()

    def getservicenameByid(self,id):
        return db.session.query(Service.sname).filter(Service.sid==id).first()

