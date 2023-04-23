from collections import defaultdict
from bankomat import Bankomat

from kommun import Kommun

class DataParser:


    def laddaKommuner(self):

        fn = "information-files/befolkningsdata/2014M1-2018M9.csv"
        fk = "information-files/befolkningsdata/2018M10-2023M1.csv"

        with open(fn, encoding="utf-8") as f:
            s = f.read()

        lines = s.splitlines()

        with open(fk, encoding="utf-8") as f:
            s = f.read()

        lines += s.splitlines()[1:]

        kommuner = [None]*300

        for i, e in enumerate(lines[0].split(";")):
            if len(e) < 2:
                continue
            num, nam = e.split(' ', 1)
            kommuner[i] = {"namn": nam, "id": num, "data": defaultdict(dict)}


        month = None
        for line in lines[1:]:
            ålder = None
            for i, e in enumerate(line.split(';')):
                if i == 0:
                    if e:
                        month = e
                elif i == 1:
                    ålder = e
                else:
                    e = int(e)
                    kommuner[i]["data"][month][ålder] = e

        kommunerd = {k["id"]: k for k in kommuner if k}
        for k, v in kommunerd.items():
            for m, md in v["data"].items():
                md["total"] = sum(md.values())


        with open("information-files/befolkningsdata/Befolkningstätheter.csv", "r") as täthetsFil: 
            befolkningstätheterText = täthetsFil.readlines()

        befolkningsTätheter = defaultdict(dict)

        for befolkningsTäthetsText in befolkningstätheterText:
            befolkningstäthetsLista = befolkningsTäthetsText.split(";")
            befolkningsTäthetsDict = {
                2014: float(befolkningstäthetsLista[1]),
                2015: float(befolkningstäthetsLista[2]),
                2016: float(befolkningstäthetsLista[3]),
                2017: float(befolkningstäthetsLista[4]),
                2018: float(befolkningstäthetsLista[5]),
                2019: float(befolkningstäthetsLista[6]),
                2020: float(befolkningstäthetsLista[7]),
                2021: float(befolkningstäthetsLista[8]),
                2022: float(befolkningstäthetsLista[9]),
            }
            befolkningsTätheter[befolkningstäthetsLista[0][5:]] = befolkningsTäthetsDict

        self.kommuner:list[Kommun] = []

        for kommun in kommunerd: 
            kommun = Kommun(namn = kommunerd[kommun]["namn"], id = kommunerd[kommun]["id"], data = kommunerd[kommun]["data"])
            kommun.beräknaSnittålder()
            kommun.sättInBefolkningsTäthet(befolkningsTätheter[kommun.namn])
            self.kommuner.append(kommun)



    def laddaBankomater(self): 

        fn = "information-files/bankomatdata/KTH Uttag och insättningar 201401-202301.csv"

        with open(fn, encoding="utf-8") as bankomatFil:
            bankomatRader = bankomatFil.readlines()

        bankomatRaderUppdelade: list[list[str]] = []

        for bankomatRad in bankomatRader[1:]: 
            bankomatRaderUppdelade.append(bankomatRad.split(";"))

        index = -1

        nuvarandeId = ""

        bankomatLista: list[list[str]] = []
        self.bankomater: list[Bankomat] = []

        for uppdeladBankomatRad in bankomatRaderUppdelade: 
            if nuvarandeId == uppdeladBankomatRad[0]:
                bankomatLista[index].append(uppdeladBankomatRad)
                self.bankomater[index].läggTillTransaktion(uppdeladBankomatRad[7], int(uppdeladBankomatRad[10].replace(" ", "")), uppdeladBankomatRad[9], int(uppdeladBankomatRad[11].replace(" ", "")))
            else: 
                if index != -1:
                    self.bankomater[index-1].beräknaGenomsnittligOmsättning()
                nuvarandeId = uppdeladBankomatRad[0]
                bankomatLista.append([uppdeladBankomatRad])
                if uppdeladBankomatRad[6] == "Utomhus":
                    ärUte = True
                else: ärUte = False
                self.bankomater.append(Bankomat(uppdeladBankomatRad[0], uppdeladBankomatRad[1], uppdeladBankomatRad[2], uppdeladBankomatRad[3], uppdeladBankomatRad[4], uppdeladBankomatRad[5], ärUte))
                index += 1
                self.bankomater[index].läggTillTransaktion(uppdeladBankomatRad[7], int(uppdeladBankomatRad[10].replace(" ", "")), uppdeladBankomatRad[9], int(uppdeladBankomatRad[11].replace(" ", "")))
        else: 
            self.bankomater[index-1].beräknaGenomsnittligOmsättning()
            self.bankomater[index].beräknaGenomsnittligOmsättning()
        