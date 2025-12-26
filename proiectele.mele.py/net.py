rezervare = {
    "nume client":"Ana Popescu",
    "persoane": 4, 
    "data" : "15.12.2024",
    "ora" : "19:00",
    "mese": {
        "interior":2, 
        "terasa": 0
    },
    "meniu special" : True
}

print(f"Toata rezervarea este : {rezervare}")

rezervare["persoane"] = 6
rezervare["mese"]["terasa"] = rezervare["mese"]["terase"] +1
