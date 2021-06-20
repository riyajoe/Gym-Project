from models.Client import Client
from app import db

class clientdbController:
    def __init__(self):
        self=self
    def addClient(self,Client):
        db.create_all()
        db.session.add(Client)
        db.session.commit()
    def getClients(self):
        return db.session.query(Client).all()
    def getClientByid(self,id):
        return db.session.query.filter(Client.memberid==id)
    def getClientByMembership(self,id):
        return db.session.query(Client.membership).filter(Client.memberid==id).all()
    def updateClientByMembership(self,id,membershipObj):
        db.session.query(Client.membership).filter(Client.memberid==id).update({Client.membership:membershipObj}).all()
        db.session.commit()

          

    
