class Csoport:
    def __init__(self, nev:str, evfolyam:int, atlag:str):
        self.nev = nev
        daraboltNev = nev.split(" ")
        self.vezeteknev = daraboltNev[0]
        self.keresztnev = daraboltNev[1]
        self.evfolyam = int(evfolyam)
        atlag = atlag.replace(",",".")
        self.atlag = atlag



    def __str__(self) -> str:
        szoveg = f"Név: {self.nev}\nÉvfolyam: {self.evfolyam}\nÁtlag: {self.atlag}\n"
        return szoveg





