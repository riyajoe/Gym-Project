from app import app,db
from flask import render_template
from models.Packages import *
from models.Helper import *
#rom models.Classes import *
from DBcontroller.productdbController import productdbController
from DBcontroller.servicedbController import servicedbController

from models.Users import *
from controller.usercontroller import usercontroller

@app.route('/Package')
def Package():
    db.create_all()
    item=Helper()

    item.invoker(HIITDirector.construct())
    item.invoker(TherapyDirector.construct())
    item.invoker(DietPlanDirector.construct())
    item.invoker(YogaDirector.construct())
    item.invoker(ZumbaDirector.construct())
    item.invoker(CrossfitDirector.construct())
    item.invoker(SteamDirector.construct())
    item.invoker(SwimmingDirector.construct())
    item.invoker(CalesthenicsDirector.construct())

    productcreator=productdbController()
    wid=productcreator.addProduct(WellnessDirector.construct())
    gid=productcreator.addProduct(WeightGainDirector.construct())
    lid=productcreator.addProduct(WeightLossDirector.construct())

    servicecreator=servicedbController()
    servicecreator.addService(YogaDirector.construct(),wid)
    servicecreator.addService(TherapyDirector.construct(),wid)
    servicecreator.addService(ZumbaDirector.construct(),wid)

    servicecreator.addService(TherapyDirector.construct(),gid)
    servicecreator.addService(HIITDirector.construct(),gid)
    servicecreator.addService(DietPlanDirector.construct(),gid)
    servicecreator.addService(SteamDirector.construct(),gid)

    servicecreator.addService(SwimmingDirector.construct(),lid)
    servicecreator.addService(CalesthenicsDirector.construct(),lid)
    servicecreator.addService(CrossfitDirector.construct(),lid)
    servicecreator.addService(DietPlanDirector.construct(),lid)
    servicecreator.addService(HIITDirector.construct(),lid)
    servicecreator.addService(ZumbaDirector.construct(),lid)


    trainer=Users("trainer@test.com","test",0)
    trainerObj= usercontroller()
    trainerObj.saveuserDetails(trainer)

    

    result=Packages.query.all()   
    return(render_template('Menu.html',data=result))
 



