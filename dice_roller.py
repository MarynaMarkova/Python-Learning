from random import randint

num_dice = int(input("How many dice you want to roll? "))
num_sides = int(input("How many sides each die will have? "))

while True:
    result = "|"
    for die in range(num_dice):
        rand = randint(1, num_sides)
        result += f"{rand}|"
    print(result)
    reply = input("Roll again? (q to quit)")
    if reply == "q":
        break
