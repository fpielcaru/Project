a = [3, 7, 1, 9, 2 , 4 , 5 , 12]
odd = []
even = []
for num in a:
    if num % 2 == 0:
        even.append(num)
    else: 
        odd.append(num)
print("odds numbers:", odd)
print("even numbers:", even)