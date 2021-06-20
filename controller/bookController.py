from DBcontroller.bookdbController import bookdbController
from models.Book import Book

class bookController:
    def __init__(self):
        self=self
    
    def createBooking(self,userid,classid):
        BookObj=bookdbController()
        test=Book(memberId=userid,classId=classid,bookingStatus="BOOKED")
        BookObj.addBooking(test)


    def clientBookList(self,userid):
        BookObj=bookdbController()
        self.data=BookObj.fetchCustomisedBooking(userid)
        return self.data

    def cancelBooking(self,userid,classid):
        BookObj=bookdbController()  
        BookObj.cancelBookingByUserId(userid,classid) 

    def ListAllBookings(self):
        BookObj=bookdbController()  
        self.data=BookObj.fetchAll() 
        return self.data

