#PyPoll
import os
import csv

print("-------------------------")
orig_csv = os.path.join('python-challenge/PyPoll/Resources', 'election_data.csv')
output = "python-challenge/PyPoll/Analysis/answers.txt"
#VARIABLES
votes = 0
candidates = []
c_votes = {}
count = 0
winner = ""

#OPEN FILE
with open(orig_csv) as csvfile:
    csvreader = csv.DictReader(csvfile)
    csv_header = next(csvreader)
    #LOOP THRU ROWS
    for row in csvreader:
        votes += 1
        candidate = row["Candidate"]
        # if statement to run on first occurence of candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            c_votes[candidate] = 1
        c_votes[candidate] = c_votes[candidate] + 1
#WRITE TO FILE
with open(output, 'w') as file:
    print("Election Results")
    file.write("Election Results\n")
    print("-------------------------")
    file.write("-------------------------\n")
    print("Total Votes: " + str(votes))
    print("-------------------------")
    file.write("Total Votes:  %s\n" % votes)
    file.write("-------------------------\n")  

    for candidate in c_votes:
        can_votes = c_votes[candidate]
        vote_percentage = float(can_votes)/float(votes)*100
        if (can_votes > count):
            count = can_votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({can_votes-1})\n"
        print(voter_output)
        file.write(voter_output)
    file.write("-------------------------\n")
    print("-------------------------")
    print("Winner: " + winner)
    file.write("Winner: %s\n" % winner)
    file.write("-------------------------\n")
 
        
    
