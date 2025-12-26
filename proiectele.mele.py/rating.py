ratinguri = [4.5, 2.0, 5.0, 3.5, 1.0, 4.0]

print("STATUS RATING")
print("=" *15)

for i in ratinguri:
    if i >= 4.0:
        print(f"{i}: Produs recomandat!")
    else:
        print(f"{i}: Produs nerecomandat!")

print("=" *15)