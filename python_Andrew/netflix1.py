# import the file netflix_ratings.csv
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# set path for file
csvpath = os.path.join("python_Andrew","netflix_ratings.csv")

# open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # loop through looking for the video
    for row in csvreader:
        if row[0] == video:
            print(row[0] + " is rated " + row[1] + " with a rating of " + row[5])

    # If the video isn't found, alert the user
    if found is False:
        print("Sorry, we don't seem to have what you're looking for. ")



