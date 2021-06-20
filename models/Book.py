from app import db 

class Book(db.Model):
    BookingId=db.Column(db.Integer,primary_key=True)
    memberId=db.Column(db.Integer)
    classId=db.Column(db.String(20))
    bookingStatus=db.Column(db.String(20))
    def __init__(self,memberId=None,classId=None,bookingStatus=None):
        self.memberId=memberId
        self.classId=classId
        self.bookingStatus=bookingStatus
    def BookClass(self):
        db.create_all()
        db.session.add(self)
        db.session.commit()
        
