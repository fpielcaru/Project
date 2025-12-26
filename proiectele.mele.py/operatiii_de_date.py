propozitie = input("Introdu o propozitie: ")

propozitie_mare = propozitie.upper()
cuvinte = propozitie.split()
numar_cuvinte = len(cuvinte)
primul_cuvant = cuvinte[0]

print(f"propozitie in majuscule: {propozitie_mare}")
print(f"numar de cuvinte: {numar_cuvinte}")
print(f"primul = cuvant: {primul_cuvant}")
print(f"toate cuvintele: {cuvinte}")