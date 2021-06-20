from builder.ServiceBuilder import ServiceBuilder
class HIITDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S104")\
            .setName("HIIT")\
            .setPrice(100)\
            .createBundle()\
            .setType('S')\
            .setTag('WL')\
            .setTrainer('Jerry Holden')       