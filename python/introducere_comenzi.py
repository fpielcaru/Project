while True:
    # Introducerea numarului de produse
    try:
        numar_produse = int(input("Introdu numarul de produse din comanda: "))
    except ValueError:
        print("Eroare: Te rog introdu un număr valid.")
        continue

    if numar_produse < 1 or numar_produse > 50:
        print("Eroare: Numar de produse invalid.")
        continue

    # Introducerea pretului comenzii
    try:
        pret_comanda = float(input("Introdu pretul comenzii: "))
    except ValueError:
        print("Eroare: Te rog introdu un pret valid.")
        continue

    if pret_comanda <= 0:
        print("Eroare: Pretul trebuie sa fie mai mare decât 0.")
        continue

    # Introducerea statusului platii
    status_plata = input("Introdu statusul platii (platit / neplatit / in asteptare): ").strip().lower()

    if status_plata == "platit":
        print(f"\nComanda este valida si poate fi procesata!")
        print(f"Numar de produse: {numar_produse}, preț: {pret_comanda}, status plata: {status_plata}")
        break
    elif status_plata in ["neplatit", "in asteptare"]:
        print("Comanda nu este platita, nu poate fi procesata.")
        continue
    else:
        print("Eroare: Status de platad necunoscut.")
        continue
