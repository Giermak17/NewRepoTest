# make initial variable to track game play
user_play = "y"

# Set start number (Bonus)
start_number = 0

# while we are still playing
while user_play == "y":

    # ask the user how many numbers to loop through
    user_number = int(input("How many numbers? "))

    # Loop through the numbers. Be sure to cast the string into an integer. Now updated for bonus, to start where the previous loop ended
    for x in range(start_number, int(user_number) + start_number):

        # Print each number in the range
        print(x)
    
    # Set the next start number as the last number of the loop (Bonus)
    start_number = start_number + int(user_number)

    # Complete, ask to play again
    user_play = input("Continue: (y)es or (n)o? ")
