#Python Weight Converter

weight = float(input("Enter your weight:"))
unit = input("Kilograms or Pound? (K/P): ")

if unit == "K" :
    weight = weight * 2.2205
    unit = "Lbs."
elif unit == "L" :
    weight = weight / 2.2205
    unit = "Kgs."
else :
    print(f"{unit} was not valid")

print(f"Your weight is {weight} {unit}")