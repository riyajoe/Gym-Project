from app import app,db
from flask import render_template,request
from displayfactory.ProductFactory import *
from models.Users import requires_roles

@app.route('/PackageDetails',methods=['GET','POST'])
def PackageDetails():
    packagelist=['Wellness','WeightLoss','WeightGain']
    for i in packagelist:
            try:
                label=request.form[i]
                print(i)
            except:
                pass        
    if(label=="Wellness"):
        #@app.route('/WellnessPackage')
        #def WellnessPackage():
        print(label)
        enumlist=[]
        testObj=ProductFactory.getProductType("Wellness")
        enumlist= testObj.getProduct()
        return(render_template('Wellness.html',data=enumlist))
    elif(label=="WeightLoss"):
        enumlist=[]
        testObj=ProductFactory.getProductType("WeightLoss")
        enumlist= testObj.getProduct()
        return(render_template('WeightLoss.html',data=enumlist))    
    
    elif(label=="WeightGain"):
        enumlist=[]
        testObj=ProductFactory.getProductType("WeightGain")
        enumlist= testObj.getProduct()
        return(render_template('WeightGain.html',data=enumlist))               