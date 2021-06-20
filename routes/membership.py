from flask import render_template,flash,redirect,url_for
from models.Packages import *
from models.Helper import *
from app import app,db
from controller.usercontroller import usercontroller
from controller.clientcontroller import clientcontroller

import forms
@app.route('/Register',methods=['POST','GET'])
def Register():
    form=forms.RegistrationForm()
    if form.validate_on_submit():
        userObj=usercontroller()
        userObj.registerUser(form)
        userid=userObj.getUserid(form.email.data)
        client=clientcontroller()
        client.registerclient(form,userid)
        flash("sucessfully registered")
        return redirect(url_for('login'))
    return(render_template('Register.html',form=form))