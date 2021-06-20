from displayfactory.WellnessFactory import WellnessFactory
from displayfactory.WeightLossFactory import WeightLossFactory
from displayfactory.WeightGainFactory import WeightGainFactory

class ProductFactory():
    @staticmethod
    def getProductType(productType):
        if productType =="Wellness":
            return WellnessFactory()
        elif productType =="WeightLoss":
            return WeightLossFactory()
        else:
            return WeightGainFactory()