from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField,SubmitField,IntegerField,PasswordField,validators,DateTimeField,FloatField,TimeField,DateField
from flask import Flask, request



class RegistrationForm(FlaskForm):
    name=StringField('name')
    email=StringField('email')
    password=StringField('password')
    membership=StringField('membership')
    duration=IntegerField('duration')
    submit=SubmitField('submit')

class RoutineForm(FlaskForm):
    classid=StringField('classid')
    scheduledDate=DateField('scheduledDate')
    startTime=TimeField('startTime')
    endTime=TimeField('endTime')
    SpacesAvailable=IntegerField('SpacesAvailable')
    ServiceId=StringField('ServiceId')
    Create=SubmitField('Create Routine')    


class LoginForm(FlaskForm):
    email = StringField('email')
    password = PasswordField('password')
    submit = SubmitField('Login')    

class BMIForm(FlaskForm):
    height=FloatField('height')
    weight=FloatField('weight')
    age=IntegerField('age')
    submit = SubmitField('Check')

class ModificationForm(FlaskForm):
    classId=StringField('classId')
    modify=SubmitField('Modify')

class timeModificationForm(FlaskForm):
    startTime=TimeField('startTime')
    endTime=TimeField('endTime')
    modify=SubmitField('Modify')    

class dateModificationForm(FlaskForm):
    schduledDate=DateField('schduledDate')
    modify=SubmitField('Modify')

class SpaceModifcationForm(FlaskForm):
    spaces=IntegerField('spaces')
    modify=SubmitField('Modify')

class TrainerModificationForm(FlaskForm):
    trainer=StringField('trainer')
    modify=SubmitField('Modify')

