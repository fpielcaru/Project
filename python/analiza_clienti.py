# Datele introduse direct în script
clienti_luni = 230
clienti_marti = 200
clienti_miercuri = 310
clienti_joi = 290
clienti_vineri = 400
clienti_sambata = 150
clienti_duminica = 180

# Calculul numărului total de clienți pentru săptămână
total_saptamana = clienti_luni + clienti_marti + clienti_miercuri + clienti_joi + clienti_vineri + clienti_sambata + clienti_duminica
print(f"Numărul total de clienți pentru săptămână: {total_saptamana}")

# Calculul numărului total de clienți pentru zilele lucrătoare
total_zile_lucratoare = clienti_luni + clienti_marti + clienti_miercuri + clienti_joi + clienti_vineri
print(f"Numărul total de clienți pentru zilele lucrătoare: {total_zile_lucratoare}")

# Calculul numărului total de clienți pentru weekend
total_weekend = clienti_sambata + clienti_duminica
print(f"Numărul total de clienți pentru weekend: {total_weekend}")

# Compararea duminică vs sâmbătă (if pe o singură linie)
print("Duminică a fost o zi de vânzări mai bună decât sâmbătă") if clienti_duminica > clienti_sambata else print("Sâmbătă a fost o zi de vânzări mai bună decât duminică")

# Compararea zilelor lucrătoare vs weekend
if total_zile_lucratoare > total_weekend:
    print("Zilele lucrătoare au avut mai mulți clienți decât weekend-ul")
else:
    print("Weekend-ul a avut mai mulți clienți decât zilele lucrătoare")

# Verificarea condiției pentru ambele zile de weekend
if clienti_sambata > 100 and clienti_duminica > 100:
    print("Ambele zile de weekend au avut mai mult de 100 de clienți")
elif clienti_sambata > 100 or clienti_duminica > 100:
    print("Doar o zi de weekend a avut mai mult de 100 de clienți")
else:
    print("Nici o zi de weekend nu a avut mai mult de 100 de clienți")