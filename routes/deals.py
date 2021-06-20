from app import app,db
from flask import render_template
from displayfactory.ProductFactory import *
from models.Users import requires_roles

@app.route('/Deals')
def Deals():
    ItemList=[]
    ResultList={}
    packagelist=['Wellness','WeightLoss','WeightGain']
    for i in packagelist:
        testObj=ProductFactory.getProductType(i)
        ItemList=testObj.getProduct()
        sum=testObj.getPrice(ItemList)
        ResultList[i]=sum
        #ResultList.append(sum)
        #return(render_template('Deals.html',data=ItemList))
    return(render_template('Deals.html',data=ResultList))