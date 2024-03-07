import module1

def kuvaa_valikud():
    print("\nValikud:")
    print("1. Kasutaja registreerimine")
    print("2. Kasutaja autoriseerimine")
    print("3. Nime või parooli muutmine")
    print("4. Unustatud parooli taastamine")
    print("5. Lõpetamine")

def kasutaja_registreerimine(kasutajate_nimekiri):
    kasutajanimi = input("Sisesta kasutajanimi: ")
    parooli_valik = input("Kas soovid automaatset parooli (A) või luua ise (I)? ").upper()
    if parooli_valik == "A":
        parool = module1.genereeri_parool()
    elif parooli_valik == "I":
        parool = module1.käsitsi_parool()
    else:
        print("Vale valik!")
        return
    module1.registreeri_kasutaja(kasutajanimi, parool, kasutajate_nimekiri)

def kasutaja_autoriseerimine(kasutajate_nimekiri):
    kasutajanimi = input("Sisesta kasutajanimi: ")
    parool = input("Sisesta parool: ")
    if kasutajanimi in kasutajate_nimekiri and kasutajate_nimekiri[kasutajanimi] == parool:
        print("Autentimine õnnestus!")
    else:
        print("Vale kasutajanimi või parool!")

def nime_või_parooli_muutmine():
    print("Valik veel rakendamata.")

def unustatud_parooli_taastamine():
    print("Valik veel rakendamata.")

kasutajate_nimekiri = {}

while True:
    kuvaa_valikud()
    valik = input("Vali tegevus: ")

    if valik == "1":
        kasutaja_registreerimine(kasutajate_nimekiri)

    elif valik == "2":
        kasutaja_autoriseerimine(kasutajate_nimekiri)

    elif valik == "3":
        nime_või_parooli_muutmine()

    elif valik == "4":
        unustatud_parooli_taastamine()

    elif valik == "5":
        break

    else:
        print("Vale valik!")