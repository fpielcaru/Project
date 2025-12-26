text = input("Introdu un text: ")

if text == text.upper():
    tip_text = "SCRIE PREA TARE"
elif text == text.lower():
    tip_text = "SCRIS URÂT"
elif text.istitle():  # ✅ Verifică dacă fiecare cuvânt începe cu majusculă
    tip_text = "SCRIS FRUMOS"
else:
    tip_text = "SCRIS NORMAL"

print("\n=== ANALIZA TEXT ===")
print(f"Textul este: {tip_text}")