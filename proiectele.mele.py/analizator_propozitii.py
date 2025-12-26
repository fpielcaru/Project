propozitie = ("Python este un limaj de programare popular.")
cuvinte = propozitie.split()
caractere = len(propozitie)
numar_cuvinte = len(cuvinte)
primele_c = cuvinte[:5]
primele_c4 = " ".join(primele_c)

print(f"numarul de caractere in propozitie este: {caractere}, numarul de cuvinte este: {numar_cuvinte}, propozitia formata din primele 4 cuvinte este: {primele_c4}")