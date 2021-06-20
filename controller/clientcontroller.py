from models.Client import Client
from DBcontroller.clientdbController import clientdbController
from app import db
from datetime import date

class clientcontroller:
    def getDetails(self,form,userid):
        client=Client()
        client.memberid=userid
        client.membername=form.name.data
        client.membership=form.membership.data
        client.billedAmount=1000
        client.status="Active"
        client.membershipOpenDate=date.today()
        if form.duration.data==6:
            client.membershipCloseDate=date.today()
        elif form.duration.data ==3:
            client.membershipCloseDate=date.today()
        else:
            client.membershipCloseDate=date.today()
        return client
  
    def saveclientDetails(self,client):
        appDB= clientdbController()
        appDB.addClient(client)




    def registerclient(self,form,userid):
        data=self.getDetails(form,userid)
        self.saveclientDetails(data)
    

    def getClientmembershipById(self,userid):
        acess= clientdbController()
        membershiptype=acess.getClientByMembership(userid)
        return membershiptype
    #praveen use this function for membership updation
    def upgradeMembershipById(self,userid,membershipObj):
        acess= clientdbController()
        acess.updateClientByMembership(userid,membershipObj)
        return "updated"
