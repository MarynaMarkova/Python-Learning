from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1, 3)

# Turn that random number into the computer's RPS move
if num == 1:
    move = rock
elif num == 2:
    move = paper
else:
    move = scissors

# Ask a user to enter their move

user_move = input("Enter your move (rock, paper or scissors): ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move

if user_move == "rock":
    user_move = rock
elif user_move == "paper":
    user_move = paper
else:
    user_move = scissors


print(
    f"""Your move:
{user_move}

"""
)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print(
    f"""Computer move:
{move}

"""
)

# Figure out who wins and print the result!
if user_move == move:
    print(
        """
    =============
     IT'S A TIE!
    =============
    """
    )
elif (
    (user_move == rock and move == paper)
    or (user_move == paper and move == scissors)
    or (user_move == scissors and move == rock)
):
    print(
        """
    =============
    Computer win!
    =============
    """
    )
else:
    print(
        """
    =============
      You WIN!!!
    =============
    """
    )
