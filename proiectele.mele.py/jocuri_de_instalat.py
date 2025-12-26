jocuri = ["Minecraft", "Fortnite", "CS:GO", "Valorant", "GTA V"]
total_jocuri = len(jocuri)
print(f"Jocuri de instalat: {total_jocuri}")

for joc in range(len(jocuri)):
    print(f"Jocul {joc+1}/{total_jocuri}: {jocuri[joc]} a fost instalat cu succes!")