from functools import wraps
from app import db,login
from flask_user import UserMixin
from flask_login import current_user
from werkzeug.security import generate_password_hash, check_password_hash




class Users(db.Model,UserMixin):
    userid=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(30),unique=True)
    password=db.Column(db.String(30))
    role=db.Column(db.Integer)

    def __init__(self,email=None,password=None,role=None):
        self.email=email
        self.password=password
        self.role=role

    def checkPassword(self, password):
        if self.password ==password:
        #return check_password_hash(self.password, password)
            return True

    def get_id(self):
           return (self.userid)

    def getUserRole(self):
           return (self.role)        

@login.user_loader
def load_user(emailid):
    user = Users.query.filter_by(email=emailid).first()
    return user    

def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if current_user.role not in roles:
                # Redirect the user to an unauthorized notice!
                return "You are not authorized to access this page"
            return f(*args, **kwargs)
        return wrapped
    return wrapper        