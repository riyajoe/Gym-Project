
from builder.ProductBuilder  import ProductBuilder
class WeightGainDirector:
    @staticmethod
    def construct():
        return ProductBuilder()\
            .setId("P231")\
            .setName("WeightGain")\
            .setPrice(400)\
            .createBundle()\
            .setType('P')\
            .setTag('NIL')\
            .setTrainer('Mixed Trainers')      