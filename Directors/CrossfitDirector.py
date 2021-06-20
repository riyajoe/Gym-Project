from builder.ServiceBuilder import ServiceBuilder
class CrossfitDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S102")\
            .setName("Crossfit")\
            .setPrice(400)\
            .createBundle()\
            .setType('S')\
            .setTag('WL')\
            .setTrainer('Byron Hendrich')       