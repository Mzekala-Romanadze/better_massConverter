
unit = input("T or KG? ").upper()
while unit != "T" and unit != "KG":
	unit = input("Invalid input. Enter 'T' or 'KG'" ).upper()

amount = float(input("Amount: "))

if unit == "T":
	print(f"{amount * 1000} KG.")

elif unit == "KG":
	print(f"{amount / 1000} KG.")

