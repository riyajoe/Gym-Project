from app import db

class Service(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    sid = db.Column(db.String(20))
    pid=db.Column(db.String(20))
    sname = db.Column(db.String(50))
    sprice = db.Column(db.Float)
    trainer=db.Column(db.String(20))
def __init__(self,sid=None,pid=None,sname=None,sprice=None,trainer=None):
    self.sid=sid
    self.pid=pid
    self.sname=sname
    self.sprice=sprice
    self.trainer=trainer
       