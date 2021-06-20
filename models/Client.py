from app import db
from datetime import date
class Client(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    memberid=db.Column(db.Integer)
    membername=db.Column(db.String(20))
    membership=db.Column(db.String(30))
    status=db.Column(db.String(20))
    membershipOpenDate=db.Column(db.Date)
    membershipCloseDate=db.Column(db.Date)
    billedAmount=db.Column(db.Integer)

    def __init__(self,memberid=None,membername=None,membership=None,status="Active",membershipOpenDate=date.today(),membershipCloseDate=None):
        self.memberid=memberid
        self.membername=membername
        self.membership=membership
        self.status=status
        self.membershipOpenDate=membershipOpenDate
        self.membershipCloseDate=membershipCloseDate   