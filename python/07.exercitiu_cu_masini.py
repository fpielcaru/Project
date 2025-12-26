# cod eronat
tip_masina = "electric"
loc_parcare = "standard"
ore_parcare = "2"
abonament_activ = False 
if tip_masina == "handicap":
    print("poate parca oriunde")
if tip_masina == "electric":
    print("poate parca doar in locuri electric")
if tip_masina == "standard":
    print("poate parca doar in locuri standard")
elif loc_parcare == ("handicap"):
    print("parcarer permisa")
elif loc_parcare == ("electric"):
    print("parcare innaccesibila")
elif loc_parcare == ("electric"):
    print("parcare indisponibila")
if ore_parcare == 2:
    print("Activ!")
elif ore_parcare == 5:
    print("parcare interzisa!")

#cod compact 
tip_masina = "electric"
loc_parcare = "standard"
ore_parcare = 2
abonament_activ = False

if (tip_masina == "handicap" or
    (tip_masina == "electric" and loc_parcare in ["electric", "standard"]) or
    (tip_masina == "standard" and loc_parcare == "standard")):
    
    if ore_parcare > 3 and not abonament_activ:
        print("Parcare interzisa")
    else:
        print("Parcare permisa")
else:
    print("Parcare interzisa")