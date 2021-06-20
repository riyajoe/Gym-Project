from app import app,db
from flask import render_template,request
from models.Packages import *
from models.Helper import *
#from models.Classes import *

@app.route('/Schedule',methods=['POST','GET'])
def Schedule():
    #result=Classes.query.all()
    if request.method=='POST':
        return(render_template('Schedule.html'))