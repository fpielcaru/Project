studenti = ["Ana", "Bogdan", "Cristina", "David", "Elena", "Florin"]

numar_total = len(studenti)
print(f"Total studenti: {numar_total}")

for i in range(len(studenti)):
    print(f"Studentul {i+1}/{numar_total}: {studenti[i]} este prezent")