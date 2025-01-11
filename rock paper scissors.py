import random

def get_choices():
 player_choice=input("enter a choice(rock,paper,scissors):")
 options=["rock","paper","scissors"]
 computer_choice=random.choice(options)
 return{"player":player_choice,"computer":computer_choice}
def check_win(player,computer):
  print(f"you choose{player},computerchoose{computer}")
  if player==computer:
    return "it's a tie!"
  elif player=="rock":
    if computer=="paper":
      return "paper covers rock,you lose"
    else:
      return "rock smashes paper,you win!"
  elif player=="paper":
    if computer=="rock":
      return "paper covers rock,you win!"
    else:
      return "scissors cuts paper,you lose."
  elif player=="scissors":
    if computer=="rock":
      return "rock smashes paper,you lose."
    else:
      return "scissors cuts paper,you win!"

choices= get_choices()
result= check_win(choices["player"],choices["computer"])
print(result)
