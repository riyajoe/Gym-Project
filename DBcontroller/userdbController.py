from models.Users import Users
from app import db
class userdbController:
    def __init__(self):
        self=self
    def addUser(self,Users):
        db.create_all()
        db.session.add(Users)
        db.session.commit()
    def getUsers(self):
        return db.session.query(Users).all()
    def getUserIdByemail(self,emailid):
        return db.session.query(Users.userid).filter(Users.email== emailid).all()
 

