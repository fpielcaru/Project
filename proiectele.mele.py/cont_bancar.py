cont = {
    "titular" : "Alex Popescu", 
    "sold" : 5000,
    "valuta" : "RON", 
    "tip_cont" : "curent"
}

print("Datele clientului nostru:")

cont["sold"] = cont["sold"] + 1500
cont["sold"] = cont["sold"] - 800
cont["tip_cont"] = "economii"

if "sold" > "2000 RON":
    print("Soldul este peste 2000 RON")
else:
    print("Soldul este sub 2000 RON")

cont["sold"] = cont["sold"] % 5

print(f"{cont}")