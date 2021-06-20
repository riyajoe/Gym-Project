from models.DailySchedule import DailySchedule
from DBcontroller.dailysheduledbController import dailyscheduledbController

class schedulecontroller:
    def __init__(self):
        self=self

    def getScheduleInfo(self,form):
        
        ScheduleObj=DailySchedule()
        ScheduleObj.classId=form.classid.data
        ScheduleObj.scheduledDate=form.scheduledDate.data
        ScheduleObj.startTime=form.startTime.data
        ScheduleObj.endTime=form.endTime.data
        ScheduleObj.SpacesAvailable=form.SpacesAvailable.data
        ScheduleObj.ServiceId=form.ServiceId.data
        ScheduleObj.Status="OPEN"
        return ScheduleObj

    def saveSchedule(self,obj):
        appobj=dailyscheduledbController()
        appobj.addSlot(obj)

    def SlotInfo(self,classid):
        appobj=dailyscheduledbController()
        data=appobj.getclassinfoByclassId(classid)
        return data

    def addspace(self,classid):
        appobj=dailyscheduledbController()
        appobj.addcount(classid)

    def fillspace(self,classid):
        appobj=dailyscheduledbController()
        appobj.decrementcount(classid)  

    def cancelslotbyId(self,classid):
        appobj=dailyscheduledbController()
        appobj.cancelslot(classid)
        return "action performed" 

    def getMaximumSpaces(self,classid):
        appobj=dailyscheduledbController()
        self.maxcount=appobj.getspaces(classid)
        print(self.maxcount)
        return self.maxcount
    
        
        