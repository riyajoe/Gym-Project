from builder.ServiceBuilder import ServiceBuilder
class SteamDirector:
    @staticmethod
    def construct():
        return ServiceBuilder()\
            .setId("S105")\
            .setName("Steaming Service")\
            .setPrice(100)\
            .createBundle()\
            .setType('S')\
            .setTag('WG')\
            .setTrainer('Self Service')        