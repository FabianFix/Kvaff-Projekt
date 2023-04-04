class Bankomat: 
    def __init__(self, automatId: int, address: str, postkod: int, postort: str, kommun: str, län: str, ärUte: bool, perioderSEK: list[int], transaktionerSEK: list[int], omsättningSEK: list[int], perioderAnnan: list[int], transaktionerAnnan: list[int], omsättningAnnan: list[int]) -> None:
        
        self.id = automatId

        self.geographicalData = {
            "address": address,
            "postkod": postkod,
            "postort": postort,
            "kommun": kommun,
            "län": län
        }

        self.ärUte = ärUte
        self.transaktionsDataSEK = {}
        self.transaktionsDataAnnan = {}

        index = 0
        for period in perioderSEK: 
            self.transaktionsDataSEK[period] = {
                "antalTransaktioner": transaktionerSEK[index],
                "omsättning": omsättningSEK[index],
            }
            index += 1
            
        index = 0
        for period in perioderAnnan: 
            self.transaktionsDataAnnan[period] = {
                "antalTransaktioner": transaktionerAnnan[index],
                "omsättning": omsättningAnnan[index],
            }
            index += 1

    def hämtaPopulation(self) -> None:
        pass