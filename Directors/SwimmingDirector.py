from builder.ServiceBuilder import ServiceBuilder
class SwimmingDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S127")\
            .setName("Swimming Service")\
            .setPrice(100)\
            .createBundle()\
            .setType('S')\
            .setTag('WL')\
            .setTrainer('Adam Hastings')       