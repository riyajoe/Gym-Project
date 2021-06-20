
from models.Product import *
from app import db

class productdbController:
    def __init__(self):
        self=self
    def addProduct(self,Prodbj):
        db.create_all()
        print(Prodbj.id,Prodbj.name,Prodbj.price,Prodbj.trainer)
        Prod=Product(pid=Prodbj.id,pname=Prodbj.name,price=Prodbj.price,trainer=Prodbj.trainer)
        db.session.add(Prod)
        db.session.commit()
        return Prodbj.id
        