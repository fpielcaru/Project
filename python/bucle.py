lei = 997
euro = 500
lei_ramasi = 563
euro_ramasi = 157

while (lei > euro) and (euro_ramasi > 200):
    lei_ramasi += 10; euro_ramasi -= 98  # folosim punct-virgulă

print(f"total_bani : {lei_ramasi}, {euro_ramasi}")
print("arata")