# print the first text
print("Hello user!")
# make a variable to loop the question
user_play = "y"
while user_play == "y":
    # make a variable, take the input from a question
    name = input("What is your name? ")
    # Then respond with the name included
    print("Hello " + name+", nice to meet your acquaintance." )
    # ask age
    age = input("What is your age? ")
    # then respond from two choices depending on age input
    if (int(age) < 40):
        print("You are just a baby. ")
    if (int(age) >= 40):
        print("A well traveled soul are ye. ")
    
    # ask to continue
    user_play = input("Continue: (y)es or (n)o ")
