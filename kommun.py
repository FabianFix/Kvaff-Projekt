class Kommun: 
    def __init__(self, namn: str, id: str, data: dict[str: dict[str: int]]) -> None:
        self.namn = namn
        self.id = id
        self.data = data
        self.antalBankomater = 0

    def beräknaSnittålder(self):
        self.sistaNyckeln = list(self.data.keys())[-1]
        self.sistaVärdet = list(self.data.values())[-1]
        totalÅlder = 0
        snittÅlderFörGruppen = 9.5
        for värde in list(self.sistaVärdet.values())[0:9]:
            totalÅlder += värde * snittÅlderFörGruppen
            snittÅlderFörGruppen += 10
        
        self.snittÅlder = round(totalÅlder / self.data[self.sistaNyckeln]["total"])

    def sättInBefolkningsTäthet(self, befolkningstätheter: dict[int, float]):
        self.befolkningstätheter = befolkningstätheter

    def __str__(self) -> str:
        return f"Kommunen {self.namn} har id {self.id} och har som senast totalt {self.data['2023M01']['total']} människor som bodde i kommunen. Snittåldern är {round(self.snittÅlder)} år, samt hade år 2017 en befolkningstäthet på: {round(self.befolkningstätheter[2017])} människor/km^2"