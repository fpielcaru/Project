distante = [2, 15, 8, 25, 5, 30]

print("VERIFICARE BILETE")
print("/" * 20)

for km in distante:
    if km <= 5:
        print(f"{km}: Bilet urban")
    elif km >= 20:
        print(f"{km}: Bilet regional")
    else:
        print(f"{km}: Bilet interregional")


print("/" *20)