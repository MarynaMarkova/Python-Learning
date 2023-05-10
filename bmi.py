height = float(input("Enter your height in inches! "))
weight = float(input("Enter your weight in pounds! "))

BMI = weight * 703 / height**2
BMI = round(BMI, 1)

if BMI < 16.0:
    category = "severly underweight"
elif BMI < 18.4:
    category = "underweight"
elif BMI < 24.9:
    category = "normal"
elif BMI < 29.9:
    category = "overweight"
elif BMI < 34.9:
    category = "moderately obese"
elif BMI < 39.9:
    category = "severely obese"
else:
    category = "morbidly obese"

print(f"Your BMI of {BMI} makes you {category}!")
