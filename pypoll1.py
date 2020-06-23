# import csv file
import os
import csv

filepath = os.path.join("learnpython","election_data1.csv")

# set arrays, variables
Candidate = []
Candidate_Name = []
Percent = []

Candidate_Votes = 0

# read file, header
with open("election_data1.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# append each column
    for row in csvreader:
        Candidate.append(row[2])

# find the total votes
Total_Votes = len(Candidate)

# get candidate list
Candidate_Name = set(Candidate)

# get number of votes for each candidate 
for Name in Candidate_Name:
    Candidate_Votes[Name] = 0

Result = zip(Voter_ID, Candidate)

for Voter_ID, Candidate in Result:
    if Candidate in Candidate_Votes:
        Candidate_Votes[Candidate] += 1

Winner = max(zip(Candidate_Votes.keys()))
