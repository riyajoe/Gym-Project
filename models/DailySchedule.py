from app import db

class DailySchedule(db.Model):
    classId=db.Column(db.String(20),primary_key=True)
    scheduledDate=db.Column(db.Date)
    startTime=db.Column(db.Time)
    endTime=db.Column(db.Time)
    SpacesAvailable=db.Column(db.Integer)
    ServiceId=db.Column(db.String(20))
    Status=db.Column(db.String(20))
    def __init__(self,classId=None,scheduledDate=None,startTime=None,endTime=None,SpacesAvailable=None,ServiceId=None,Status="OPEN"):
        self.classId=classId
        self.scheduledDate=scheduledDate
        self.startTime=startTime
        self.endTime=endTime
        self.SpacesAvailable=SpacesAvailable
        self.ServiceId=ServiceId
        self.Status="OPEN"
