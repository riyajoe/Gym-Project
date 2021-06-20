from models.DailySchedule import DailySchedule
from app import db
class dailyscheduledbController:
    def __init__(self):
        self=self
    
    def getallclassinfo(self):
        return db.session.query(DailySchedule).all()
    def getSlotInfo(self,classid):
        return db.session.query(DailySchedule.ServiceId).filter(DailySchedule.classId==classid).all()
    def updateSpaces(self,classid):
        return db.session.query(DailySchedule).filter(DailySchedule.classId == classid).update({DailySchedule.SpacesAvailable:DailySchedule.SpacesAvailable-1})

    def addSlot(self,DailySchedule):
        db.create_all()
        db.session.add(DailySchedule)
        db.session.commit()

    def getclassinfoByServiceId(self,ServiceId):
        return db.session.query(DailySchedule.classId).filter(DailySchedule.ServiceId==ServiceId).all()

    def getclassinfoByclassId(self,classid):
        return db.session.query(DailySchedule).filter(DailySchedule.classId==classid).first()   
        
    def addcount(self,classid):
        db.session.query(DailySchedule).filter(DailySchedule.classId == classid).update({DailySchedule.SpacesAvailable:DailySchedule.SpacesAvailable+1})
        db.session.commit()
    def decrementcount(self,classid):
        db.session.query(DailySchedule).filter(DailySchedule.classId == classid).update({DailySchedule.SpacesAvailable:DailySchedule.SpacesAvailable-1})
        db.session.commit()
    def cancelslot(self,classid):
        db.session.query(DailySchedule).filter(DailySchedule.classId == classid).update({DailySchedule.Status:'CANCELLED'})
        db.session.commit()
    def getspaces(self,classid):
        return db.session.query(DailySchedule.SpacesAvailable).filter(DailySchedule.classId==classid).all()  
         
