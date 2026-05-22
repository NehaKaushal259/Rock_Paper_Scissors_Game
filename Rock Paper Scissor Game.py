"""
WORKFLOW OF PROJECT:
1- Input From User(Rock, Paper, Scissor)
2- Computer Choice (computer will choose randomly not conditionally)
3- Result Print

Cases:

A - ROCK
Rock - Rock = tie
Rock - Paper = Paper win
Rock - Scissor = Rock win

B - PAPER
Paper - Paper = tie
Paper - Rock = Paper Win
Paper - Scissor - Scissor Win

C - SCISSOR
Scissor - Scissor = tie
Scissor - Rock = Rock Win
Scissor - Paper = Scissor Win

"""


import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter Your Choice (Rock, Paper, Scissor) = ")
comp_choice = random.choice(item_list)

print(f"User Choice is = {user_choice}, Computer Choice is = {comp_choice}")


if user_choice == comp_choice:
    print("Both Chooses Same : Match Tie")


elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper Covers Rock : Computer Win")
    else:
        print("Rock Samashes Scissor : You Win")


elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper Covers Rock : You Win")
    else:
        print("Scissor Cuts Paper : Computer Win")


elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock Smashes Scissor : Computer Win")
    else:
        print("Scissor Cuts Paper : You Win")
