import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join("learnpython", "wrestling.csv")

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(data):

    name = str(data[0])
    wins = int(data[1])
    losses = int(data[2])
    draws = int(data[3])

# Find the total number of matches wrestled
    total = wins + losses + draws

# Find the percentage of matches won
    win_percent = (wins / total) * 100

# Find the percentage of matches lost
    loss_percent = (losses / total) * 100

# Find the percentage of matches drawn
    draw_percent = (draws / total) * 100

# Print out the wrestler's name and their percentage stats
    print(f"Stats for {name}")
    print(f"Win Percent: {str(win_percent)}")
    print(f"Loss Percent: {str(loss_percent)}")
    print(f"Draw Percent: {str(draw_percent)}")


# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
