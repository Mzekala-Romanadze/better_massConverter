
unit = input("T or KG? ").upper()
while unit != "T" or unit != "KG":
	unit = input("Invalid input. Enter 'T' or 'KG'" ).upper()

amount = float(input("Amount: "))

if unit == "T":
	print(f"{amount * 1000} Kg.")

elif unit == "KG":
	print(f"{amount / 1000} Kg.")

else:
	print("Error!")
