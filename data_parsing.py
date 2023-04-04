from collections import defaultdict

from kommun import Kommun

class DataParser:
    def __init__(self):

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

        self.kommuner = []

        for kommun in kommunerd: 
            kommun = Kommun(namn = kommunerd[kommun]["namn"], id = kommunerd[kommun]["id"], data = kommunerd[kommun]["data"])
            self.kommuner.append(kommun)
