telefon = {
    "brand" : "Samsung", 
    "model" : "Galaxy S21", 
    "stocare" : 128, 
    "pret" : 2500, 
    "culoare" : "negru"
}

print("Telefon initial:")

telefon["pret"] = telefon["pret"] + 200
telefon["culoare"] = "albastru"
telefon["garantie"] = "24 luni"
if telefon["stocare"] <= 128:
    print("Telefonul are 128 GB")
else:
    print("Telefonul nu are 128 GB")

telefon["pret"] = telefon["pret"] + telefon["pret"] * 19 

print(f"{telefon}")