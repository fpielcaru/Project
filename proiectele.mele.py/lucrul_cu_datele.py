a = int(input("introdu primul nr:"))
f = int(input("introdu al doilea nr:"))
k = int(input("introdu al treilea nr:"))

if a >= f and a >= k:
    print(f"{a} este cel mai mare numar")
elif f >=a and f>=k:
    print(f"{f} este cel mai mare numar")
else:
    print(f"{k} este cel mai mare numar")