from app import db
from DBcontroller.servicedbController import servicedbController


class Display(db.Model):
    classid=db.Column(db.String(20),primary_key=True)
    servicename=db.Column(db.String(50))
    scheduleddate=db.Column(db.Date)
    starttime=db.Column(db.Time)
    endtime=db.Column(db.Time)
    trainer=db.Column(db.String(50))
    spaces=db.Column(db.Integer)
    classtatus=db.Column(db.String(20))

    def __init__(self,classid=None,servicename=None,scheduleddate=None,starttime=None,endtime=None,trainer=None,spaces=None,classtatus=None):
        self.classid=classid
        self.servicename=servicename
        self.scheduleddate=scheduleddate
        self.starttime=starttime
        self.endtime=endtime
        self.trainer=trainer
        self.spaces=spaces
        self.classtatus=classtatus

    def getdisplayinforByServiceId(self,sid):
        obj=servicedbController()
        data=obj.getservicenameByid(sid)
        return db.session.query(Display).filter(Display.servicename==data,Display.classtatus =="OPEN").all()

    def getdisplayinforByClassId(self,classid):
        obj=servicedbController()
        return db.session.query(Display).filter(Display.classid==classid).all()    

    
    def addcount(self,classid):
        db.session.query(Display).filter(Display.classid == classid).update({Display.spaces:Display.spaces+1})
        db.session.commit()
    def decrementcount(self,classid):
        db.session.query(Display).filter(Display.classid == classid).update({Display.spaces:Display.spaces-1})
        db.session.commit()
    def cancelslot(self,classid):
        db.session.query(Display).filter(Display.classid == classid).update({Display.classtatus:'CANCELLED'})
        db.session.commit()
    def getcount(self,classid):
        return db.session.query(Display.spaces).filter(Display.classid==classid).all() 

