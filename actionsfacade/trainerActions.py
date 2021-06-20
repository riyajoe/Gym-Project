from models.display import Display
from controller.schedulecontroller import schedulecontroller
import forms
class TrainerActions:
    def __init__(self):
        self=self
    def cancelClass(self,classid):
        revert=Display()
        cancelSchedule=schedulecontroller()
        revert.cancelslot(classid)
        mesg=cancelSchedule.cancelslotbyId(classid)
        print(mesg)

    def modifyClass(self,classid,tag):
        if tag=="Trainer":
            self.form=forms.TrainerModificationForm()
            

        elif tag == "Date":
            self.form=forms.dateModificationForm()


        elif tag == "Start-time" or tag =="End-time":
            self.form=forms.timeModificationForm()

        else:
            self.form=forms.SpaceModifcationForm() 
        return self.form
