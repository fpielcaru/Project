masina = {
    "marca" : "Volkswagen", 
    "model" : "Golf",
    "an" : 2018, 
    "problema" : "distributie", 
    "cost_reparatie" : 1500
}

print("Masina initiala")

masina["problema"] = "distributie + ulei"
masina["durata_reparatiei"] = "3 zile"

if masina["cost_reparatie"] > 1000:
    print("Costul reparatiei depaseste 1000 de lei!")
else: 
    print("Costul reparatiei nu depaseste 1000 de lei!")

del masina["an"]

print(f"{masina}")