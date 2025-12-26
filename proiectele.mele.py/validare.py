contor = 0
numar = 1

print("introdu numere:22")

while numar != 0:
    numar = int(input("Introdu un numar:"))
    if numar >= 4:
        contor = contor +1
        print(f"numarul {numar} a fost procesat, contor: {contor}")

print(f"numere mai mari saua egal cu 4: {contor}")