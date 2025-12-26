stoc_produse = 45
timp_lucru_ramas = 6

while stoc_produse >= 5 and timp_lucru_ramas > 0:
   stoc_produse -= 4
timp_lucru_ramas -=1 
if stoc_produse < 15:
    print("Stocul este sub 15 unitati!")

print(f"Stoc: {stoc_produse} , Timp ramas: {timp_lucru_ramas} ore ")
if stoc_produse < 5:
    print("stoc epuizat - vanzarile sunt oprite")
if timp_lucru_ramas <= 0:
    print("tinmpul de lucru s-a terminat")