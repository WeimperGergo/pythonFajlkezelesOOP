import Csoport

adatokLista = []


def beOlvas():
    beFajl = open("forras/csoport.txt", "r", encoding="utf-8")
    # 1. sor
    beFajl.readline()
    sorok = beFajl.readlines()
    for sor in sorok:
        tisztitottSor = sor.strip()
        # -/m
        darabolt = tisztitottSor.split("/")
        # / mentén elemek
        csoportTag = Csoport.Csoport(darabolt[0], int(darabolt[1]), darabolt[2])
        print(csoportTag)
        adatokLista.append(csoportTag)
    beFajl.close()

def kiir():
    for i in range(0, len(adatokLista), 1):
        print(adatokLista[i])

def sorokSzama():
    sorszam = len(adatokLista)
    print(f"A tanulók száma: {sorszam}.")

def megszamlalas():
    osszeg = 0
    for i in range(0, len(adatokLista), 1):
        osszeg += float(adatokLista[i].atlag)

    if len(adatokLista) == 0:
        atlag = 0
    else:
        atlag = osszeg/len(adatokLista)
    print(f"Az iskola átlaga: {atlag}")

def elsosok():
    elsosDb = 0
    for i in range(0, len(adatokLista), 1):
        if adatokLista[i].evfolyam == 1:
            elsosDb += 1
    print(f"{elsosDb} elsős van.")

def maxAtlag():
    legnagyobb = 0
    for i in range(0, len(adatokLista), 1):
        legnagyobb = adatokLista[0].atlag
        if legnagyobb < adatokLista[i].atlag:
            legnagyobb = adatokLista[i].atlag
    print(f"Legnagyobb átlag: {legnagyobb}")
# FŐPROGRAM

beOlvas()
kiir()
sorokSzama()
megszamlalas()
elsosok()
maxAtlag()
