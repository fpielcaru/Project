carte = {
    "autor" : "Marin Preda",
    "an" : 1965,
    "titlu" : "La Galeteni", 
    "pret" : "20 ron", 
}

print("Carte initiala:" , carte)

carte["pagini"] = 361
print("Dupa adaugare pagini:", carte)

optiune_carte = {"coperta" , "scris lizibil" , "editura", "text aldin", "coperta"}
print("Optiuni disponibile:", optiune_carte)

optiune_cautata = "coperta"
if optiune_cautata in optiune_carte:
    print(f"optiunea '{optiune_cautata}' este in stoc")
else:
    print(f"Optiunea '{optiune_cautata}' nu este in stoc")

optiune_cautata2 = "ilustratii"
if optiune_cautata2 in optiune_carte:
    print(f"optiunea '{optiune_cautata2}' este disponibila")
else:
    print(f"optiunea '{optiune_cautata2}' nu este disponibila")