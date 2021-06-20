from ProductFactory import ProductFactory
itemGridListAll=[]
class GridMenu:
   
    def __init__(self):
        self.itemGridListAll=[]
        self.LatestList=[]
        self.itemGridListAll.append("Wellness")
        self.itemGridListAll.append("WeightLoss")
        self.itemGridListAll.append("WeightGain")
    def  DisplayItems(self):
        for i in self.itemGridListAll:
            package=ProductFactory.getProductType(i)
            self.Items=package.getProduct()
            sum=0
            for eachitem in self.Items:
                sum=sum+eachitem.price
                self.LatestList.append(eachitem)

        return(self.LatestList)    
        
