from app import db

class Packages(db.Model):
    pid = db.Column(db.String(20),primary_key = True)
    name = db.Column(db.String(50))
    price = db.Column(db.Float)
    packagetype = db.Column(db.String(20))
    tag = db.Column(db.String(20))
    trainer=db.Column(db.String(20))

    def __init__ (self, pid=None, name=None, price=None, packagetype=None, tag=None,trainer=None):
        self.pid = pid
        self.name = name
        self.price = price
        self.packagetype = packagetype
        self.tag = tag
        self.trainer=trainer

    def addpackages(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()    


