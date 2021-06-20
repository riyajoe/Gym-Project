from controller.clientcontroller import clientcontroller
from controller.usercontroller import usercontroller
membershiptype=[]
class startegycontroller:
    def __init__(self):
        self=self
    
    def initaitebooking(self,membershiptype):
    
        
        if membershiptype == 'Platinum':
            self.memberproduct=['P103','P111','P231']
            return self.memberproduct
        elif membershiptype =='Gold':
            self.memberproduct=['P111','P103']
            return self.memberproduct
        else:
            self.memberproduct=['P103']
            return self.memberproduct

    