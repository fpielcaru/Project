sex = input("introduceti sexul (M/F):").upper()
varsta = int(input("introduceti varsta:"))


if varsta > 70:
    print("acces interzis")
elif sex == "M" and varsta < 18:
    print("accesc interzis")
elif sex == "F" and varsta < 16:
    print("acces interzis")
else:
    print("acces permis")