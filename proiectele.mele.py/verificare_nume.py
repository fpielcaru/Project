def numara_vocale(nume):
    vocale = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    contor = 0

    for caracter in nume:
        if caracter in vocale:
            contor += 1

    return contor 

while True:
    nume = input("Introdu numele clientului: ")
    numar_vocale = numara_vocale(nume)

    if numar_vocale > 0:
        print(f"Numele '{nume}' are {numar_vocale}")
    else:
        print(f"Numele nu contine vocale. Programul se incheie")
        break