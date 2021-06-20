class Service():
    def __init__(self, id=1, name="Steam",price=100,type='S',tag="W",trainer="David Henry"):
        self.id = id
        self.name = name
        self.price = price
        self.type=type
        self.tag=tag
        self.trainer=trainer
    def __str__(self):
        return "The Bundle rendered with service id {0} name is {1} priced at  Euro :{2}.".format(self.id,self.name,self.price)   
         