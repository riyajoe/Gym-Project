from builder.ServiceBuilder  import ServiceBuilder
class YogaDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S110")\
            .setName("Yoga")\
            .setPrice(200)\
            .createBundle()\
            .setType('S')\
            .setTag('WLL')\
            .setTrainer('Yana Gupta')        