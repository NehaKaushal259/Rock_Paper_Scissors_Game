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




from tkinter import *
import random

# main Window
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("500x500")


item_list = ["Rock", "Paper", "Scissor"]


# Score Variables
user_score = 0
comp_score = 0
round_number = 1



# Result variable
result_text = StringVar()
result_text.set("Choose Rock, paper or Scissor")




# Game Function

def play(user_choice):
    global user_score
    global comp_score
    global round_number

    comp_choice = random.choice(item_list)

    result = (
        f"\n ------- Round {round_number} -------\n\n"
        f"User Choice = {user_choice}\n"
        f"Computer Choice = {comp_choice}\n\n"
    )



    # # Input Validation
    # if user_choice not in item_list:
    #     print("Invalid Input! Choose Rock, paper or Scissor.")
    # else:
    #     comp_choice = random.choice(item_list)



    if user_choice == comp_choice:
        result += "Both Chooses Same : Match Tie"

        with open("scores.txt", "a") as file:
            file.write("Match Tie\n")


    elif user_choice == "Rock":
        if comp_choice == "Paper":
            result += "Paper Covers Rock : Computer Win"
            comp_score += 1

            with open("scores.txt", "a") as file:
                file.write("Computer Won\n")

        else:
            result += "Rock Samashes Scissor : You Win"
            user_score += 1

            with open("scores.txt", "a") as file:
                file.write("User Won\n")


    elif user_choice == "Paper":
        if comp_choice == "Rock":
            result += "Paper Covers Rock : You Win"
            user_score += 1

            with open("scores.txt", "a") as file:
                file.write("User Won\n")

        else:
            result += "Scissor Cuts Paper : Computer Win"
            comp_score += 1

            with open("scores.txt", "a") as file:
                file.write("Computer Won\n")


    elif user_choice == "Scissor":
        if comp_choice == "Rock":
            result += "Rock Smashes Scissor : Computer Win"
            comp_score += 1

            with open("scores.txt", "a") as file:
                file.write("Computer Won\n")

        else:
            result += "Scissor Cuts Paper : You Win"
            user_score += 1

            with open("scores.txt", "a") as file:
                file.write("User Won\n")



    # ScoreBoard
    result += (
        f"\n\n------- Score Board -------\n"
        f"Your Score = {user_score}\n"
        f"Computer Score = {comp_score}"
    )

    result_text.set(result)

    round_number += 1


    # # Replay Option 
    # play_again = input("\n Do You Want To Play Again? (yes/no) = ")
    # if play_again.lower() != "yes":
    #     print("\n Game Over!")
    #     break





# Heading
Label(
    root,
    text="Rock paper Scissors Game",
    font=("Arial", 20, "bold")
).pack(pady=20)


# Result Label
Label(
    root,
    textvariable=result_text,
    font=("Arial", 12),
    justify=LEFT
).pack(pady=20)


# Buttons
Button(
    root,
    text="Rock",
    width=20,
    command=lambda: play("Rock")
).pack(pady=10)
    
Button(
    root,
    text="Paper",
    width=20,
    command=lambda: play("Paper")
).pack(pady=10)

Button(
    root,
    text="Scissor",
    width=20,
    command=lambda: play("Scissor")
).pack(pady=10)



# Run Window
root.mainloop()