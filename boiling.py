unit = input("What unit are you using: f, c or k? ")
temp = int(input("What temperature is the water? "))
boiling = "The water is boiling"
not_boiling = "The water is not boiling"

if unit == "f":
    if temp < 212:
        print(not_boiling)
    else:
        print(boiling)
elif unit == "c":
    if temp < 100:
        print(not_boiling)
    else:
        print(boiling)
else:
    if temp < 373:
        print(not_boiling)
    else:
        print(boiling)
