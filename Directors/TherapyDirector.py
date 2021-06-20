from builder.ServiceBuilder import ServiceBuilder
class TherapyDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S119")\
            .setName("Therapy")\
            .setPrice(200)\
            .createBundle()\
            .setType('S')\
            .setTag('WG,WELL')\
            .setTrainer('Dr Matilda Philps')       