from interface.IFactory import IFactory
from Directors.CrossfitDirector import *
from Directors.WeightLossDirector import *
from Directors.YogaDirector import *
from Directors.SteamDirector import *
from Directors.CalesthenicsDirector import *
from Directors.CrossfitDirector import *
from Directors.DietPlanDirector import *
from Directors.HIITDirector import *
from Directors.SwimmingDirector import *
from Directors.TherapyDirector import *
from Directors.ZumbaDirector import *
from Directors.WellnessDirector import *
from Directors.WeightLossDirector import *
from Directors.WeightGainDirector import *

class WeightLossFactory(IFactory):
    def __init__(self):
        self.completeList=[]
        self.listname=[]
    def getProduct(self):
        #self.completeList.append(WeightLossDirector.construct())
        self.completeList.append(SwimmingDirector.construct())
        self.completeList.append(CalesthenicsDirector.construct())
        self.completeList.append(CrossfitDirector.construct())
        self.completeList.append(DietPlanDirector.construct())
        self.completeList.append(HIITDirector.construct())
        self.completeList.append(ZumbaDirector.construct())
        return(self.completeList)
        
    def getPrice(self,completeList):
        self.sum=0
        for i in self.completeList:
            self.sum=self.sum+i.price
        return(self.sum)
    def getName(self,completeList):
        for i in self.completeList:
            self.listname.append(i.name)  
        return(self.listname)             