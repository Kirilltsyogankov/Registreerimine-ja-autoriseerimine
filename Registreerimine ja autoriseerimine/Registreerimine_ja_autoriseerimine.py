import random
import string

def registreeri_kasutaja(nimi, parool, kasutajate_nimekiri):
    if nimi in kasutajate_nimekiri:
        print("Kasutajanimi on juba kasutusel!")
        return False
    kasutajate_nimekiri[nimi] = parool
    print("Kasutaja registreeritud edukalt!")
    return True

def genereeri_parool(pikkus=8):
    erimargid = ".,:;!_*-+"
    numbrid = '0123456789'
    vaiketahed = 'qwertyuiopasdfghjklzxcvbnm'
    suurtahed = vaiketahed.upper()
    koik_tahed = erimargid + numbrid + vaiketahed + suurtahed
    tahed = list(koik_tahed)
    random.shuffle(tahed)
    parool = ''.join([random.valik(tahed) for x in range(pikkus)])
    return parool

def käsitsi_parool():
    while True:
        parool = input("Sisesta parool: ")
        if len(parool) < 8:
            print("Parool peab olema vähemalt 8 tähemärki pikk!")
        if not any(taht.isdigit() for taht in parool):
            print("Parool peab sisaldama vähemalt üht numbrit!")
        if not any(taht.islower() for taht in parool):
            print("Parool peab sisaldama vähemalt üht väiketähte!")
        if not any(taht.isupper() for taht in parool):
            print("Parool peab sisaldama vähemalt üht suurtähte!")
        if not any(taht in string.punctuation for taht in parool):
            print("Parool peab sisaldama vähemalt üht erimärki!")
        return parool