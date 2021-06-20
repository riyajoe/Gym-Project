from builder.ProductBuilder  import ProductBuilder
class WeightLossDirector:
    @staticmethod
    def construct():
        return ProductBuilder()\
            .setId("P111")\
            .setName("WeightLoss")\
            .setPrice(400)\
            .createBundle() \
            .setType('P')\
            .setTag('NIL')\
            .setTrainer('Mixed Trainers')           