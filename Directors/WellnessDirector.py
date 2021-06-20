from builder.ProductBuilder  import ProductBuilder
class WellnessDirector:
    @staticmethod
    def construct():
        return ProductBuilder()\
            .setId("P103")\
            .setName("Wellness")\
            .setPrice(600)\
            .createBundle()\
            .setType('P')\
            .setTag('NIL')\
            .setTrainer('Mixed Trainers')          