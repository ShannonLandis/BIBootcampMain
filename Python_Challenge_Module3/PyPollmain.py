#Python Challenge Module 3 - Part 2
# PyPoll
# Shannon Landis
# December 27, 223


# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote



# import libraries
import os
import csv


#read election_data file stored in Resources folder and set output path/file
#electiondata_csv = os.path.join("..", "Resources", "election_data.csv")
electiondata_csv = os.path.join("Resources", "election_data.csv")
output_path = os.path.join("analysis", "PyPoll_Results.txt")


# create list
candidateRow = []
candidateList = [] # will store unique candidate list
candidateTally = []  # store tally for writing to text file
winnerList = [] #storing winner in list so it can be written to text file

# open file note comma delimiter and skip header row
with open(electiondata_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader) 


    # Read through each row of data after the header and append values to lists
    for row in csv_reader:
        candidateRow.append(row[2])

# set totalVotes to length of list
totalVotes = len(candidateRow)


#function to create a unique list of unique candidates - appends to new list if not already there
def uniqueCandidates(candidates):
    
    for candidate in candidateRow:
        if candidate not in candidateList:
            candidateList.append(candidate)
    return candidateList


#funtion to tally votes, calc percentage won, and determine winner
def tallyVotes(candidates):
    maxVotes = 0
    winningCandidate = ""
    candidateVotes = 0
    

    for candidate in set(candidateList):
        #keep track of candidate with most votes to determine winner
        candidateVotes = candidateRow.count(candidate)
        if candidateRow.count(candidate) > maxVotes:
            winningCandidate = candidate
            maxVotes = candidateRow.count(candidate)

        #calculate percent votes won per candidate
        percentVotes = round((candidateRow.count(candidate)/totalVotes)*100,3)
    
        #print row with candidate name, percent votes won and count of votes won
        print(f"{candidate}:  {percentVotes}% ({candidateRow.count(candidate)})")
        candidateTally.append(str(candidate) + ":  " +  str(percentVotes) + "%  (" + str(candidateVotes) + ")")


    
    #now that loop is complete, print the final winner and write to winner list
    print("-------------------------")
    print(f"Winner: {winningCandidate}")
    print("-------------------------")

    winnerList.append("Winner:  " + winningCandidate)

    



#print report summary rows        
print("Election Results")
print("-------------------------")
print(f"Total Votes:  {totalVotes}")
print("-------------------------")

# call functions to get unique list and tally votes
result = uniqueCandidates([candidateRow]) #passes list of all candidates
result = tallyVotes(candidateList) # passes unique list of candidates



#Open text file to write out results
with open(output_path, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes:  {totalVotes}\n")
    txtfile.write("-------------------------\n")
    for candidates in candidateTally:
        txtfile.write(candidates)
        txtfile.write("\n")
    txtfile.write("-------------------------\n")
    for winners in winnerList:
        txtfile.write(winners)




# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


#finally close the text file just to be safe the with should close the file when complete
txtfile.close()