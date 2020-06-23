# Create an input to take - rock paper or scissors 
import random
print ("Let's play rock paper scissors!")
pick = ['r', 'p', 's'] 

# Have the computer randomly pick 1 of the 3 choices
computer_choice = random.choice(pick)
user_choice = input("Make your choice: (r)ock, (p)aper, (s)cissors  ")

# compare the user's input to the computer's random pick
# determine the user's win, loss or tie
# run all the possible conditionals, using if elif
if (user_choice == "r" and computer_choice == "p"):
    print("You chose rock. The computer chose paper.")
    print("Sorry, you lose.")

elif (user_choice == "r" and computer_choice == "s"):
    print("You chose rock. The computer chose scissors.")
    print("You win!")

elif (user_choice == "r" and computer_choice == "r"):
    print("You chose rock. The computer chose rock.")
    print("It's a draw.")

elif (user_choice == "p" and computer_choice == "s"):
    print("You chose paper. The computer chose scissors.")
    print("Sorry, you lose.")

elif (user_choice == "p" and computer_choice == "p"):
    print("You chose paper. The computer chose paper.")
    print("It's a draw.")

elif (user_choice == "p" and computer_choice == "r"):
    print("You chose paper. The computer chose rock.")
    print("You win!")

elif (user_choice == "s" and computer_choice == "p"):
    print("You chose scissors. The computer chose paper.")
    print("You win!")

elif (user_choice == "s" and computer_choice == "r"):
    print("You chose scissors. The computer chose rock.")
    print("Sorry, you lose.")

elif (user_choice == "s" and computer_choice == "s"):
    print("You chose scissors. The computer chose scissors.")
    print("It's a draw.")

# If the user inputs something else
else:
    print ("I don't understand that. ")
    print ("Next time choose 'r', 'p' or 's'.")





