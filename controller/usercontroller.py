from models.Users import Users
from DBcontroller.userdbController  import userdbController

class usercontroller:
    def __init__(self):
        self=self 
    def getUserDetails(self,form):
        userObj=Users()
        userObj.email=form.email.data
        userObj.password=form.password.data
        userObj.role=1
        return userObj
    def saveuserDetails(self,user):
        appDB= userdbController()
        appDB.addUser(user)
    
    def registerUser(self,form):
        data=self.getUserDetails(form)
        self.saveuserDetails(data)

    def getUserid(self,email):
        appDB= userdbController()
        userId=appDB.getUserIdByemail(email)
        return userId
        

