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
        self.transaktionsDataSEK: list[dict] = []
        self.transaktionsDataEUR: list[dict] = []
        self.transaktionsDataUSD: list[dict] = []

    def __str__(self) -> str:
        return f"Bankomat med id {self.id}, som finns på addressen {self.geographicalData['address']}, i {self.geographicalData['kommun']} kommun. Det finns {len(self.transaktionsDataSEK) + len(self.transaktionsDataUSD) + len(self.transaktionsDataEUR)} transaktionsadata registrerade. ÄrUte = {self.ärUte}"
    
    def läggTillTransaktion(self, månad:str, antalTransaktioner:int, valuta:str, omsättning:int): 
        if valuta == "SEK":
            self.transaktionsDataSEK.append({
                "månad": månad[0:4] + "M" + månad[4:],
                "antalTransaktioner": antalTransaktioner,
                "omsättning": omsättning
            })
        
        if valuta == "USD":
            self.transaktionsDataUSD.append({
                "månad": månad[0:4] + "M" + månad[4:],
                "antalTransaktioner": antalTransaktioner,
                "omsättning": omsättning
            })
        
        if valuta == "EUR":
            self.transaktionsDataEUR.append({
                "månad": månad[0:4] + "M" + månad[4:],
                "antalTransaktioner": antalTransaktioner,
                "omsättning": omsättning
            })

    def beräknaGenomsnittligOmsättning(self): 
        self.totalOmsättning = 0
        self.antalMånader = max([len(transaktionsData) for transaktionsData in [self.transaktionsDataSEK + self.transaktionsDataEUR + self.transaktionsDataUSD]])

        for transaktion in self.transaktionsDataSEK + self.transaktionsDataEUR + self.transaktionsDataUSD:
            self.totalOmsättning += transaktion["omsättning"]

        self.genomsnittligOmsättning = round(self.totalOmsättning / self.antalMånader)
        