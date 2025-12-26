# ==============================
# Proiect final: Analiza clienților
# ==============================

def citeste_nume():
    """
    Solicită numele complet până când utilizatorul introduce
    cel puțin două cuvinte.
    """
    while True:
        nume_complet = input("Introduceți numele și prenumele: ").strip()
        if " " in nume_complet:
            parti = nume_complet.split()
            if len(parti) >= 2:
                return parti[0], parti[1]
        print("❌ Numele nu a fost introdus corect. Încercați din nou.")


def determina_statut(total_cheltuit, nr_achizitii):
    """
    Determină statutul utilizatorului.
    """
    if total_cheltuit > 100000 and nr_achizitii > 10:
        return "VIP"
    else:
        return "STANDARD"


# 1️⃣ Citire nume și prenume
nume, prenume = citeste_nume()

# 2️⃣ Număr achiziții
nr_achizitii = int(input("Introduceți numărul total de achiziții din ultimul an: "))

total_cheltuit = 0
achizitii_peste_10000 = 0

# 3️⃣ Citire sume achiziții
for i in range(1, nr_achizitii + 1):
    suma = float(input(f"Introduceți suma achiziției {i} (lei): "))
    total_cheltuit += suma

    if suma > 10000:
        achizitii_peste_10000 += 1

# 4️⃣ Determinare statut
statut = determina_statut(total_cheltuit, nr_achizitii)

# 5️⃣ Stabilire reducere
if statut == "VIP":
    reducere = 0.10
else:
    reducere = 0.05

# 6️⃣ Calcul preț cu reducere
pret_produs = float(input("Introduceți prețul produsului dorit (lei): "))
pret_final = pret_produs - (pret_produs * reducere)

# 7️⃣ Afișare rezultate
print("\n===== REZULTATE =====")
print(f"Nume client: {nume} {prenume}")
print(f"Număr total achiziții: {nr_achizitii}")
print(f"Suma totală cheltuită: {total_cheltuit:.2f} lei")
print(f"Achiziții peste 10.000 lei: {achizitii_peste_10000}")
print(f"Statut client: {statut}")
print(f"Reducere aplicată: {int(reducere * 100)}%")
print(f"Preț final cu reducere: {pret_final:.2f} lei")
