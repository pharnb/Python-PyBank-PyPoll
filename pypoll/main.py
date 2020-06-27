#* In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

#* You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create 
# a Python script that analyzes the votes and calculates each of the following:

import os
import csv

csvpath = os.path.join('resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    totalcount = 0
    votedict = {}
    votepercent = []
    winvote = 0
    i = 0

    for row in csvreader:
        #  * The total number of votes cast
        totalcount += 1
        #  * A complete list of candidates who received votes
        if row[2] not in votedict:
            votedict.update({row[2]:1})
            #print(f'{votedict}')    
        #  * The total number of votes each candidate won
        else:
            votedict[row[2]] += 1
            #print(f'{votedict}') 

#  * The percentage of votes each candidate won
#print(f'{votedict}') 
for key in votedict:
    votepercent.append(votedict[key])
#print(f'{votepercent}') 
votepercent[:] = [round(100 * i / totalcount, 3) for i in votepercent]
#print(f'{votepercent}') 
#  * The winner of the election based on popular vote.
winner = max(votedict, key=votedict.get)
#print(f'{winner}') 

#* As an example, your analysis should look similar to the one below:

print("Election Results")
print("-------------------")
print(f"Total Votes: {totalcount}")
print("-------------------")
for key in votedict:
    print(f"{key}: {votepercent[i]}% ({votedict[key]})")
    i += 1
print("-------------------")
print(f"Winner: {winner}")

#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```

#* In addition, your final script should both print the analysis to the terminal and export a text file with the results.
i = 0
file1 = open("output.txt", "a")
file1.write("Election Results\n")
file1.write("-------------------\n")
file1.write("Total Votes: %i\n" % (totalcount))
file1.write("-------------------\n")
for key in votedict:
    file1.write("%s: %5.2f%% (%i)\n" % (key, votepercent[i], votedict[key]))
    i += 1
file1.write("-------------------\n")
file1.write("Winner: %s\n" % (winner))
file1.close()