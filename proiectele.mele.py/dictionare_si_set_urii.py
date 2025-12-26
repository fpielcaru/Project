produs ={
    "nume": "Toyota",
    "model": "MK-4",
    "an de fabricatie": "1975",
    "pret": "250.000",
    "categorie": "old school"
}


print("produs initial:", produs)

produs["stare"] = "excelenta"
print("dupa adaugare stare:", produs)

optiuni_produs = {"aer conditionat", "piele alcantara", "geamuri electrice", "piele alcantara"}
print("optiuni disponibile:",  optiuni_produs)


optiuni_cautate = "navigatie"
if optiuni_cautate in optiuni_produs:
    print(f"Optiune '{optiuni_cautate}' este disponibila")
else:
    print(f"Optiunea '{optiuni_cautate}' nu este disponibila")

optiuni_cautate2 = "scaune incalzite"
if optiuni_cautate2 in optiuni_produs:
    print(f"Optiunea '{optiuni_cautate2}' este disponibila")
else:
    print(f"Optiunea '{optiuni_cautate2}' nu este disponibila")