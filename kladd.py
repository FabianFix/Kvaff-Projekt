from collections import defaultdict
import pandas as pd
from data_parsing import DataParser

data = DataParser()
data.laddaKommuner()

month = "2022M01"
year = int(month[0:4])

obj_list = []
pandan = {{
            "Befolkning": [],
            "Total Omsättning": [],
            "Omsättning per Invånare": [],
            "Antal Bankomater": [],
            "Befolknigstäthet": [],
            "Genomsnittlig Ålder": [],
            "Antal Transaktioner": [],
            "Antal Transaktioner Per Bankomat": [],
            "Genomsnittlig Transaktionsstorlek": []
        } }

for kommun in data.kommuner:
    try:
        namn = kommun.namn
        befolkning = kommun.data[month]["total"]
        totalOmsättning = kommun.totalOmsättning
        omsättningPerInvånare = kommun.omsättningPerInvånare
        antalBankomater = kommun.antalBankomater
        befolkningstäthet = kommun.befolkningstätheter[year]
        snittÅlder = kommun.snittÅlder
        antalTransaktioner = kommun.totalTransaktionsAntal
        antalTransaktionerPerBankomat = kommun.snittTransaktionsAntal
        genomsnittligTransaktionsStorlek = kommun.totalOmsättning / kommun.totalTransaktionsAntal
        
        pandan[namn] = [befolkning,totalOmsättning,omsättningPerInvånare,antalBankomater,befolkningstäthet,
                      snittÅlder,antalTransaktioner,antalTransaktionerPerBankomat,genomsnittligTransaktionsStorlek]
    except: 
        pass


df = pd.DataFrame(pandan)

print(df)