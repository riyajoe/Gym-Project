from app import db

class Product(db.Model):
    pid = db.Column(db.String(20),primary_key = True)
    pname = db.Column(db.String(50))
    price = db.Column(db.Float)
    trainer=db.Column(db.String(20))
def __init__(self,pid=None,pname=None,price=None,trainer=None):
    self.pid=pid
    self.pname=pname
    self.price=price
    self.trainer=trainer
       