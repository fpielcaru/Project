parole = ["123", "Parola123", "abc", "Secure@2026", "pass"]

print("VERIFICARE PAROLE")
print("=" * 25)

for parola in parole:
    lungime = len(parola) 

    if lungime >= 8:
        print(f"'{parola}' ({lungime} caractere): Parolă bună")
    else:
        print(f"'{parola}' ({lungime} caractere):Parolă slabă")

print("=" * 25)