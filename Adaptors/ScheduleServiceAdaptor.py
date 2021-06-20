from interface.ISchedule import ISchedule
from Adaptors.Serviceblock import Serviceblock
from controller.schedulecontroller import schedulecontroller

class ScheduleServiceAdaptor(ISchedule):
    
    def __init__(self):
        self.Service = Serviceblock()

    
    def getSchedule(self,classid):
        schObj=schedulecontroller()
        data=schObj.SlotInfo(classid)
        self.classid=classid
        self.starttime=data.startTime
        self.endtime=data.endTime
        self.schdate=data.scheduledDate
        refinedData=self.Service.getService(data.ServiceId)
        self.sname=refinedData.sname
        self.trainer=refinedData.trainer
        self.spaces=data.SpacesAvailable
        self.status=data.Status
        #return self.classid ,self.schdate,self.starttime,self.endtime,self.sname,self.trainer
        return self
  

