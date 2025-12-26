print("=== SISTEM DE CALCUL BACSIS ===")

suma_de_achitat = input("Introduceti suma de achitat: ")
bacsis = input("Introduceti procentul bacsisului dorit:  ")
bacsis_dec = float(bacsis) / 100
suma_totala = float(suma_de_achitat) + (float(suma_de_achitat)) * bacsis_dec
print(f"Suma totala de achitat este: {suma_totala}")