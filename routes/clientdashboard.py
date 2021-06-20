from app import app,db
from models.Users import requires_roles
from flask import render_template
from models.DailySchedule import DailySchedule
from flask_login import current_user
from controller.clientcontroller import clientcontroller
from controller.startegycontroller import startegycontroller 
from controller.servicecontroller import servicecontroller
from DBcontroller.dailysheduledbController import dailyscheduledbController
from Adaptors.ScheduleServiceAdaptor import ScheduleServiceAdaptor
from routes.Iterable import Iterable
import forms
from models.display import Display
from flask import request,redirect,flash
from controller.bookController import bookController
from models.Book import Book
from controller.schedulecontroller import schedulecontroller





@app.route('/ClientDashboard',methods=['POST','GET'])
def ClientDashboard():
    printtest=Iterable()
    #data=DailySchedule.query.all()
    data=[]
    collectServices=[]
    finalServices=[]
    crosscheckservices=[]
    adaptObj=ScheduleServiceAdaptor()
    retreiveObj=clientcontroller()
    userId = current_user.get_id()
    membership=printtest.convertVal(retreiveObj.getClientmembershipById(userId))
    stObj=startegycontroller()
    collectProducts=stObj.initaitebooking(membership)
    servObj=servicecontroller()
    crosscheckservices+=servObj.getservicesByProduct(collectProducts)
    displayObj=Display()
    
    for values in crosscheckservices:
        collectServices.append(values.sid)
    collectService=list(dict.fromkeys(collectServices))
    for i in collectService:
        data+=displayObj.getdisplayinforByServiceId(i)    
    
    if request.method == 'POST':
        if request.form.get('BOOK'):
            classId = request.args.get('id')
          
            print (classId)
            userId = current_user.get_id()
            BookObj=bookController()
            maxcount=displayObj.getcount(classId)
            maxcount=printtest.convertVal(maxcount)
            print(maxcount)
            
            if int(maxcount) >0:
                BookObj.createBooking(userId,classId)
                displayObj.decrementcount(classId)
                flash("BOOKING SUCESSFUL CHECK VIEW BOOKINGS")
            else:
                flash("CLASS IS FULLY BOOKED")
    return render_template('ClientDashboard.html',data=data)

@app.route('/calculateBMI')
def calculateBMI():
    form=forms.BMIForm()
    return render_template('BMI.html',form=form)

@app.route('/membershipdetails')
#write logic for member ship upgrade and downgrade using momento
def membershipdetails():
    printtest=Iterable()
    userId = current_user.get_id()
    retreiveObj=clientcontroller()
    membership=retreiveObj.getClientmembershipById(userId)
    
    return render_template('membershipdetails.html',data=printtest.convertVal(membership))

@app.route('/mybooking',methods=['POST','GET'])    
def mybooking():
    displaydata=[]
    renderdata=[]
    userId = current_user.get_id()
    BookObj=bookController()
    dispobj=Display()
    data=BookObj.clientBookList(userId)
    for i in data :
        displaydata += dispobj.getdisplayinforByClassId(i)
    
    
    if request.method == 'POST':
        printtest=Iterable()
        schObj=schedulecontroller()
        if request.form.get('CANCEL'):
            classId = request.args.get('id')
            print (classId)
            userId = current_user.get_id()
            BookObj=bookController()
            getMxcount=schObj.getMaximumSpaces(classId)
            currentcount=dispobj.getcount(classId)
            getMxcount=printtest.convertVal(getMxcount)
            currentcount=printtest.convertVal(currentcount)
            print(getMxcount,currentcount)
            getMxcount=int(getMxcount)
            currentcount=int(currentcount)
            print(getMxcount,currentcount)
            
            
            
            if currentcount<getMxcount:
                BookObj.cancelBooking(userId,classId)
                dispobj.addcount(classId)
                dataset=BookObj.clientBookList(userId)
                for i in dataset :
                    renderdata += dispobj.getdisplayinforByClassId(i)    
                return render_template('MyBooking.html',data=renderdata)
                
            else:
                flash("YOUR TRYING TO COMMIT UNAUTHORIZED ACTION")    
    return render_template('MyBooking.html',data=displaydata)          
    




