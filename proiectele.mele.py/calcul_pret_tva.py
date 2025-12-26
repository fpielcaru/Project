produs_fara_tva = input("Introduceti pretul produsului fara TVA:  ")
tva_procent = float(input("Introduceti procentul TVA-ului:  "))
tva_decimal = tva_procent / 100
pret_cu_tva = float(produs_fara_tva) + (float(produs_fara_tva)) * tva_decimal
print(f"pretul produsul cu TVA este: {pret_cu_tva}")