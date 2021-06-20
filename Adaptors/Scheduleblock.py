from interface.ISchedule import ISchedule
from controller.schedulecontroller import schedulecontroller

class Scheduleblock(ISchedule):
    "A hypothetical Cube tool from company A"
    # a static variable indicating the last time a cube was manufactured

    def __init__(self):
        self=self


    def getSchedule(self,classid):
        scheduleObj=schedulecontroller()
        data=scheduleObj.SlotInfo(classid)
        return data
        