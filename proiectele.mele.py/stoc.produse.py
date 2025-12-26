stocuri = [10, 0, 5, 3, 0 , 8]

print("VERIFICARE STOC PRODUSE")
print("=" * 6)

for g in stocuri:
    if g < 3:
        print(f"{g} stoc bun")
    elif g < 3:
        print(f"{g} stoc mic")
    else:
        print(f"{g} stoc epuizat")

print("=" *5)