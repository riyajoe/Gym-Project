from builder.ServiceBuilder import ServiceBuilder
class DietPlanDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S101")\
            .setName("Diet Plan")\
            .setPrice(250)\
            .createBundle()\
            .setType('S')\
            .setTag('WL,WG')\
            .setTrainer('Toomey Mara')        