from random import randint
from matplotlib import pyplot as plt
from data_parsing import DataParser

class AnalysModeller: 
    def __init__(self, data: DataParser) -> None:

        self.data = data

    def slumpmässigBankomatOmsättning(self):

        bankomaterIFarsta = [bankomat for bankomat in self.data.bankomater if bankomat.geographicalData["postort"] == "Farsta"]

        slumpmässigBankomat = self.data.bankomater[randint(0, len(self.data.bankomater)-1)]

        # slumpmässigBankomat = bankomaterIFarsta[randint(0, len(bankomaterIFarsta) - 1)]

        transaktionsMånader = []

        for transaktionsmånad in slumpmässigBankomat.transaktionsDataSEK:
            transaktionsMånader.append(transaktionsmånad)

        kommun = [kommun for kommun in self.data.kommuner if kommun.namn == slumpmässigBankomat.geographicalData["kommun"]][0]

        kommun.bankomaterIKommunen = [bankomat for bankomat in self.data.bankomater if bankomat.geographicalData["kommun"] == kommun.namn]

        antalBankomater = len(kommun.bankomaterIKommunen)

        månader = []
        omsättningar = []
        befolkningar = []

        for månad in transaktionsMånader:
            befolkningar.append(kommun.data[månad["månad"]]["total"] / antalBankomater)
            månader.append(månad["månad"])
            omsättningar.append(månad["omsättning"]/1000)

        plt.plot(range(len(månader)), omsättningar, befolkningar)
        plt.title(slumpmässigBankomat.geographicalData["postort"] + ", " + kommun.namn)
        plt.xlabel("månad")
        plt.legend(["Omsättning i tkr", "Antal invånare per bankomat"])

    def beräknaSnittBefolkningPerBankomat(self): 
        pass

    def scatterPlotOmsättningPerInvånare(self):
        
        omsättningar:list[int] = []
        befolkningar: list[int] = []

        for bankomat in self.data.bankomater:
            try:
                omsättningar.append(bankomat.genomsnittligOmsättning)
            except: 
                print(bankomat)
            befolkningar.append([kommun.data[kommun.sistaNyckeln]["total"] for kommun in self.data.kommuner if kommun.namn == bankomat.geographicalData["kommun"]][0])
    
        plt.scatter(befolkningar, omsättningar)
        

    def scatterPlotOmsättningPerInvånarePerBankomat(self):
        pass