#Python Weight Converter V2.0
# This program converts weight between kilograms and pounds.

weight = float(input("Enter your weight in float format:"))
unit = input("Kilograms or Pound? (K is for kgs, P is for Lbs.): ")

if unit == "K" :
    weight = weight * 2.2205
    unit = "Lbs."
elif unit == "L" :
    weight = weight / 2.2205
    unit = "Kgs."
else :
    print(f"{unit} was not valid")

print(f"Your weight is {weight} {unit}")