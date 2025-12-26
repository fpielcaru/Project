def numar_vocale(nume):
    vocale = 'aeiouAEIOU'
    contor = 0
    for caracter in nume:
        if caracter in vocale:
            contor += 1
    return contor


print("Introduceți numele clientilor. Programul se va opri cand un nume nu are vocale.\n")

while True:
    nume = input("Introduceti numele clientului: ")
    nr_vocale = numar_vocale(nume)

    # Afisam numarul de vocale
    print(f"Numele '{nume}' conține {nr_vocale} vocale.")

    # Dacă nu exista vocale, oprim programul
    if nr_vocale == 0:
        print("\nNumele introdus nu contine nicio vocala. Programul s-a incheiat.")
        break

    print("Introduceți un nou nume.\n")
