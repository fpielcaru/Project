# Program simplu pentru analiza numărului de clienți pe o săptămână

luni = int(input("Luni: "))
marti = int(input("Marți: "))
miercuri = int(input("Miercuri: "))
joi = int(input("Joi: "))
vineri = int(input("Vineri: "))
sambata = int(input("Sâmbătă: "))
duminica = int(input("Duminică: "))

# Calcule
total_saptamana = luni + marti + miercuri + joi + vineri + sambata + duminica
total_lucratoare = luni + marti + miercuri + joi + vineri
total_weekend = sambata + duminica

# Verificări
mai_multi_duminica = duminica > sambata
lucratoare_mai_multe = total_lucratoare > total_weekend
saptamana_succes = total_saptamana > 1000 or total_weekend > 500

# Rezultate
print("\n--- Rezultate ---")
print("Total săptămână:", total_saptamana)
print("Zile lucrătoare:", total_lucratoare)
print("Weekend:", total_weekend)

if mai_multi_duminica:
    print("Mai mulți clienți duminică decât sâmbătă.")
else:
    print("Mai mulți clienți sâmbătă decât duminică.")

if lucratoare_mai_multe:
    print("Zilele lucrătoare au avut mai mulți clienți decât weekendul.")
else:
    print("Weekendul a avut mai mulți clienți decât zilele lucrătoare.")

if saptamana_succes:
    print("Săptămâna a fost de succes!")
else:
    print("Săptămâna nu a fost de succes.")
