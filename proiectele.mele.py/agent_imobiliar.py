proprietate = {
    "tip" : "apartament" , 
    "camere" : 3 ,
    "suprafata" : 75,
    "zona" : "centru", 
    "pret" : 120000
}

print("Proprietate initiala:")

proprietate["pret"] = proprietate["pret"] + proprietate["pret"] * 10 / 10
proprietate["etaj"] = 5
proprietate["zona"] = "cartier rezidential"

if proprietate["suprafata"] > 70:
    print("corect")
else: 
    print("incorect")

print(f"{proprietate}")