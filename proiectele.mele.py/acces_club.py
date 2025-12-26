varsta = [17, 25, 16, 30, 19]

print("verificare acces club")
print("=" *25)

for v in varsta:
    if v < 18:
        print(f"{v} ani: nu poate intra")
    else:
        print(f"{v} ani: poate intra")

print("=" * 25)