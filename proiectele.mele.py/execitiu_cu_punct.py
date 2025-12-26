varsta_patruped = int(input("introduceti varsta partupedului"))
varsta_umana = 0
if varsta_patruped <= 2:
    varsta_umana = varsta_patruped * 10.5
    print("varsta umana a patrupedului este: ")
else:
    varsta_umana = 21 + (varsta_patruped - 2) * 4
    print(f"varsta umana a patrupedului este: {varsta_umana}")