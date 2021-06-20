from builder.ServiceBuilder import ServiceBuilder
class ZumbaDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S112")\
            .setName("Zumba")\
            .setPrice(300)\
            .createBundle()\
            .setType('S')\
            .setTag('WLL,WG')\
            .setTrainer('Merry Hawthrone')        