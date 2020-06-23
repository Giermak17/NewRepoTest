# import csv file
import os
import csv
import collections
from collections import Counter

filepath = os.path.join("learnpython","election_data1.csv")

# read file, header
with open("election_data1.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# set variables
    Vote_Count = Counter()

    Candidates = []
    County = []
    Percent = []
    Answer = []

# append Candidates
    for row in csvreader:
        Candidates.append(row[2])

# get total votes
    Total_Votes = len(Candidates)

# count votes for each candidate
    for Name in Candidates:
        Vote_Count[Name] += 1
    
    Names = tuple(Vote_Count.keys())
    
    Votes = tuple(Vote_Count.values())

    # get the percentages
    for Value in Votes:
        Percent.append((int(Value)/Total_Votes)*100)

# print everything
    Answer.append("Election Results")
    Answer.append("______")
    Answer.append("Total Votes: " + str(Total_Votes))
    Answer.append("______")
    for x in range(len(Names)):
        Answer.append(Names[x] + ": " + str(round(Percent[x], 3)) + "% " + "(" + str(Votes[x]) + ")")
    Answer.append("______")
    Answer.append("Winner: " + str(Names[0]))

    print("\n".join((Answer)))

 # create the txt file for the output
    text_path = "pypoll_results.txt"
    with open(text_path, "w") as txt_file:
        txt_file.write("Election Results" + "\r\n"
        "Total Votes: " + str(Total_Votes) + "\r\n"
        "Khan: " + str(round(Percent[0], 3)) + "% " + "(" + str(Votes[0]) + ")" + "\r\n"
        "Correy: " + str(round(Percent[1], 3)) + "% " + "(" + str(Votes[1]) + ")" + "\r\n"
        "Li: " + str(round(Percent[2], 3)) + "% " + "(" + str(Votes[2]) + ")" + "\r\n"
        "O'Tooley: " + str(round(Percent[3], 3)) + "% " + "(" + str(Votes[3]) + ")" + "\r\n"
        "Winner: " + str(Names[0]))
