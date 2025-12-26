produse = ["laptop", "mouse", "tastatura", "monitor", "cascaa"]

total_produse = len(produse)

print(f"total produse de inventariat; {total_produse}")

for i in range(len(produse)):
    print(f"produsul {i+1}/{total_produse}: '{produse[i]}' a fpst inventariat")