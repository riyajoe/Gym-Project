class Iterable:
    def __init__(self):
        self=self

    def __iter__(self):
        return iter(self)

    def convertVal(self,val):
        subval=str(val).strip('[]')
        subval=subval.replace('(','')
        subval=subval.replace(')','')
        subval=subval.replace(',', '')
        subval=subval.strip(',')
        subval=subval.replace("'", "")
        self.val=subval
        return(self.val)

    def printObj(self,data):
        self.classid=self.convertVal(data.classid)
        self.starttime=data.starttime
        self.endtime=data.endtime
        self.schdate=data.schdate
        self.sname=data.sname
        self.trainer=data.trainer
        self.spaces=data.spaces
        self.status=data.status
        print(self)
        return self