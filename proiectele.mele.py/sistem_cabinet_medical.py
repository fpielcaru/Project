pacient = {
    "nume" : "Maria Staicu",
    "varsta" : 35,
    "diagnostic" : "gripa",
    "tratament" : "paracetamol"
}

print("date_pacient:")
pacient["varsta"] = 36
pacient["diagnostic"] = "raceala usoara"
pacient["alergii"] = "nu"
del pacient["tratament"]

if pacient["varsta"] > 30:
    print("Corect")
else:
    print("Incorect!")

print(f"{pacient}")