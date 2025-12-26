varste = [16, 18, 21, 17, 20, 25]

print("VERIFICARE VARSTA DE CONDUCERE")
print("=" * 20)

for varsta in varste:
    if varsta >= 18:
        print(f"{varsta} ani: nu poate obtine permisul")
    else:
        print(f"{varsta} ani: nu poate obtine permis")

print("=" * 20)