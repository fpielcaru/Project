masina = {
    "marca":"BMW", 
    "model" : "Seria 3", 
    "an": 2020, 
    "motor": {
        "capacitate" : 2.0,
        "putere" : 184,
        "combustibil" : "benzina", 
    }, 
    "optiuni" : ["aer conditionat", "navigatie", "senzori parcare"]
}

print("masina completa:")
print(masina)

print(f"Puterea motorului este : {masina['motor']['putere']} HP")
masina["cutie"] = "automata"
masina["optiuni", ("scaune")] = "incalzite"
masina["optiuni", ("capacitate")] = 2.5

print(f"Masina are: {masina}")