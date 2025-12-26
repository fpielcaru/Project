student ={
    "nume" : "Alin Vasilescu",
    "facultate" : "automaatica", 
    "an_studiu" : 2,
    "media" : 8.75,
    "bursa" : True
}
print("Studentull initial")

student["an_studiu"] = 3
student["media"] = 9.10
student["oras"] = "Bucuresti"

if student["bursa"] == True:
    print("Are bursa!")
else:
    print("N-are bursa!")

if student["media"] > 9:
    print("corect")
else:
    print("incorect")
student["media=9"] = "bursa_merit"

print(f"{student}")