from app import app,db
from models.Users import requires_roles
from controller.schedulecontroller import schedulecontroller
from flask import render_template,request,flash,redirect,url_for
import forms
from Adaptors.ScheduleServiceAdaptor import ScheduleServiceAdaptor
from routes.Iterable import Iterable
import forms
from models.display import Display
from controller.bookController import bookController
from actionsfacade.trainerActions import TrainerActions

#from models.Classes import *
@app.route('/TrainerDashboard')
@requires_roles(0)
def TrainerDashboard():
    data=Display.query.all()
    return(render_template('TrainerLayout.html',data=data))

@app.route('/ListAllBookings')
@requires_roles(0)
def ListAllBookings():
    ListObj=bookController()
    data=ListObj.ListAllBookings()
    return(render_template('Bookings.html',data=data))

@app.route('/CreateRoutine',methods=['POST','GET'] )
@requires_roles(0)

def CreateRoutine():
    form=forms.RoutineForm()
    adaptObj=ScheduleServiceAdaptor()
    printtest=Iterable()
    if request.method=='POST':
        newschedule=schedulecontroller()
        schObj=newschedule.getScheduleInfo(form)
        newschedule.saveSchedule(schObj)
        flash("Created")
        finaldata=adaptObj.getSchedule(form.classid.data)
        resultObj=printtest.printObj(finaldata)
        obj=Display(classid=resultObj.classid,servicename=resultObj.sname,scheduleddate=resultObj.schdate,starttime=resultObj.starttime,endtime=resultObj.endtime,trainer=resultObj.trainer,spaces=resultObj.spaces,classtatus=resultObj.status)
        db.session.add(obj)
        db.session.commit()
        return redirect(url_for('TrainerDashboard'))
        
    return(render_template('Routine.html',form=form))

@app.route('/CancelRoutine',methods=['POST','GET'] )
@requires_roles(0)
def CancelRoutine():
    data=Display.query.all()
    actions=TrainerActions()
    if request.method=='POST':
        if request.form.get('CANCEL'):
            classId = request.args.get('id')
            actions.cancelClass(classId)
    return(render_template('CancelRoutineLayout.html',data=data))

@app.route('/ModifyRoutine',methods=['POST','GET'] )
@requires_roles(0)
def ModifyRoutine():
    form=forms.ModificationForm()
    trAction=TrainerActions()
    options=['Date','Start-time','End-time','Spaces','Trainer']
    if request.method =='POST':
        tag = request.form.get('data')
        classid=form.classId.data
        print(tag)
        print(classid)
        form=trAction.modifyClass(classid,tag)

        return(render_template('Modify.html',form=form))
        



    return(render_template('Modify.html',form=form,data=options))