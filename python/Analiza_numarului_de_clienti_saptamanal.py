
luni = 230
marti = 200
miercuri = 310
joi = 290
vineri = 400
sambata = 150
duminica = 180

## 01 Sa calculez numarul total de clienti
totalul_de_clienti = luni + marti + miercuri + joi + vineri + sambata + duminica
print(totalul_de_clienti)

## 02 Sa afisez numarulul de clienti in zilele lucratoare
zile_lucratoare = luni + marti + miercuri + joi + vineri
print(zile_lucratoare)

## 03 Sa afisez numarul de clienti in weekend
weekend = sambata + duminica
print(weekend)

## 04 Sa verific daca duminica au fost mai multi clienti decat sambata
duminica_mai_multi = duminica > sambata
print(duminica_mai_multi)

## 05 Sa verific daca in zilele lucratoare au fost mai multi clienti decat in weekend
zile_lucratoare_mai_multi = zile_lucratoare > weekend
print(zile_lucratoare_mai_multi)

## 06 Sa verific daca saptamana a fost una de succes (total clienti > 1000 SAU weekend > 500)
saptamana_de_succes = (totalul_de_clienti > 1000) or (weekend > 500)
print(saptamana_de_succes)
