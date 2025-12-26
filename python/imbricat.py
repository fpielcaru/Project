service = "garaj"
masina = "Toyota-MK4"
if service == "garaj":
    print("Ai rezolvat!")
    if masina > "BMW":
        print("Stai fara grija!")
    else:
        print("Ai grija!")
else: 
    print("Mai incearca odata!")
    if masina == "Toyota-MK4":
        if masina > True:
            print("Bravo")
        else:
            print("Mai baga o fisa")
    else:
        print("Stai linistit!")