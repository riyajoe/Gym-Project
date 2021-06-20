from app import app,db,login
from models.Users import Users,requires_roles
from flask_login import current_user, login_required, login_user, logout_user
from flask import render_template_string,render_template,url_for,redirect,flash,request
import forms


@login.user_loader
def user_loader(emailid):
    return Users.query.get(emailid)

# The Home page is accessible to anyone
@app.route('/',methods=['GET', 'POST'])
def login():
    form = forms.LoginForm()
    if request.method =='POST':
        if current_user.is_authenticated:
            return redirect(url_for('PackageDetails'))
        if form.validate_on_submit():
            user = Users.query.filter_by(email=form.email.data).first()
            if user and user.checkPassword(password=form.password.data):
                if user.role ==1:
                    login_user(user)
                    return redirect("/ClientDashboard")
                else:
                    login_user(user)
                    return redirect("/TrainerDashboard")
            else:
                flash('INVALID EMAIL/PASSWORD')
                return redirect(url_for('login'))
    return render_template('login.html', title='Log In', form=form)



@app.route('/logout',methods=['POST','GET'])
@login_required
@requires_roles(1,0)
def logout():
    logout_user()
    flash("logged out sucessfully")
    return(redirect(url_for('login')))
       