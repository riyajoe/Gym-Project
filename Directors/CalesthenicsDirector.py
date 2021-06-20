from builder.ServiceBuilder import ServiceBuilder
class CalesthenicsDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S100")\
            .setName("Calesthenics")\
            .setPrice(110)\
            .createBundle()\
            .setType('S')\
            .setTag('WL')\
            .setTrainer('Adam Hastings')
