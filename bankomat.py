class Bankomat: 
    def __init__(self, automatId: str, address: str, postkod: str, postort: str, kommun: str, län: str, ärUte: bool) -> None:
        
        self.id = automatId

        self.geographicalData = {
            "address": address,
            "postkod": postkod,
            "postort": postort,
            "kommun": kommun,
            "län": län
        }

        self.ärUte = ärUte
        self.transaktionsDataSEK = []
        self.transaktionsDataAnnan = []

    def __str__(self) -> str:
        return f"Bankomat med id {self.id}, som finns på addressen {self.geographicalData['address']}, i {self.geographicalData['kommun']} kommun. Det finns {len(self.transaktionsDataSEK) + len(self.transaktionsDataAnnan)} transaktionsadata registrerade. ÄrUte = {self.ärUte}"
    
    def läggTillTransaktion(self, månad:str, antalTransaktioner:int, valuta:str, omsättning:int): 
        if valuta == "SEK":
            self.transaktionsDataSEK.append({
                "månad": månad,
                "antalTransaktioner": antalTransaktioner,
                "omsättning": omsättning
            })
