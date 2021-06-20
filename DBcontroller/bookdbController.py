from models.Book import Book
from app import db

class bookdbController:
    def __init__(self):
        self=self
    def addBooking(self,Book):
        db.create_all()
        db.session.add(Book)
        db.session.commit()
    def fetchBookingDetailsbyUserId(self,userid):
        return db.session.query(Book).filter(Book.memberId==userid ,Book.bookingStatus=="BOOKED").all()
    def fetchAllBooking(self):
        return db.session.query(Book).all()
    def cancelBookingByUserId(self,userid,classid):
        db.session.query(Book.BookingId).filter(Book.memberId == userid , Book.classId == classid).update({Book.bookingStatus:"CANCELLED"})
        db.session.commit()
    def fetchCustomisedBooking(self,userid):
        return db.session.query(Book.classId).filter(Book.memberId==userid ,Book.bookingStatus=="BOOKED").all()

    def fetchAll(self):
        return db.session.query(Book).all()

