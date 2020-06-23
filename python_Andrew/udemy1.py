import os
import csv

udemy_csv = os.path.join("python test1", "web_starter.csv")

# make lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# with open
with open (udemy_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:

        # add title
        title.apepend(row[1])

        # add price
        price.append(row[4])

        # add subscribers
        subscribers.append(row[5])

        # add reviews
        reviews.append(row[6])

        # determine precent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)

        # get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

# zip lists together 
cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# set variable for output file
output_file = os.path.join("udemytest.csv")

# open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # write the header row
    wrtier.writerow()

