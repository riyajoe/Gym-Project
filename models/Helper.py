from models.Packages import Packages
from app import db
from Directors.ZumbaDirector import ZumbaDirector
from Directors.YogaDirector import YogaDirector
from Directors.WellnessDirector import WellnessDirector
from Directors.CalesthenicsDirector import CalesthenicsDirector
from Directors.WeightLossDirector import WeightLossDirector
from Directors.CrossfitDirector import CrossfitDirector
from Directors.DietPlanDirector import DietPlanDirector
from Directors.HIITDirector import HIITDirector
from Directors.SteamDirector import SteamDirector
from Directors.SwimmingDirector import SwimmingDirector
from Directors.TherapyDirector import TherapyDirector
from Directors.WeightGainDirector import WeightGainDirector

class Helper:
    def invoker(self,obj):
        value=Packages(obj.id,obj.name,obj.price,obj.type,obj.tag,obj.trainer)
        db.session.add(value)
        db.session.commit()




