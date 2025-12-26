laptop = {
    "marca" : "Dell",
    "model" : "XPS 13",
    "pret" : 4500,
    "stoc" : 15
}

print("produs initial:")

laptop["stoc"] = laptop["stoc"] + 10
laptop["pret"] = laptop["pret"] -500

laptop["garantie"] = "2 ani"

print(f"{laptop}")

if laptop["stoc"] > 0:
    print("Este in stoc!")
else:
    print("Nu este in stoc!")