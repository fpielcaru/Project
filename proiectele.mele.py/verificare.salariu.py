salarii = [2500, 1800, 3200, 1500, 2800]

print("VERIFICARE SALARIU")
print("=" *15)

for x in salarii:
    if x < 2000:
        print(f"Salariul {x} este mic")
    else:
        print(f"Salariul {x}  este bun")

print("=" *15)