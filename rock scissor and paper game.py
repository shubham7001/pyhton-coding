#Write a program for rock,paper,scissor (computer vs human)

import random
user = input("Enter a choice (rock, paper, scissors): ")
possible = ["rock","paper","scissors"]
computer = random.choice(possible)
print(f"\n user action = {user}, computer action = {computer}.\n")
if("user" == "rock"):
    if ("computer" == "scissors"):
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif ("user" == "paper"):
    if ("computer" == "rock"):
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif ("user" == "scissors"):
    if ("computer" == "paper"):
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
else:
    print("match tie")
