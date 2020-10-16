import os
import csv
import sys

# Identify filepath to import csv file to calculate election results
filepath = os.path.join("Resources","Py_Poll.csv")

# Create new lists by column as per the headings on csv file
voter_ID = []
county = []
candidate = []

# Open csv to read, seperate items by splitting with a comma, and delete the heading row to get the vote counts accurately
with open (filepath, 'r', encoding = 'utf-8') as pypoll_data:
    csvreader = csv.reader(pypoll_data, delimiter =",")
    header = next(csvreader, None)

# Put info from csv file in list
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Take off the """ for lines 25-30 if want to test the code        
"""run the code to ensure if you get the info from teh 1st row, if correct, hardcode the below and delete break    
    print(voter_ID)
    print(county)
    print(candidate)
    break
"""

# Get the total number of votes
total_vote = (len(voter_ID))

# Hard code line 24 to 28 with opening and closing """ to ensure to get the correct total count
print (total_vote)

# Need to determine the # of candidates by printing the unique list to run the for loop below
candidate_list = list(set((candidate)))
print(candidate_list)

#create empty list for the store values for the number of votes received and winning % for each candidate
candidate_vote_count =[]
candidate_percentage = []

# Insert values for vote counts for each candidate and winning %
# For Loop will go through all the rows of counting the items candidate list created in line 22 to calculate:
    # Vote Counts per candidate 
    # % Votes per candidate - candidate list count divide (line 22) by the total vote (line 33)
# Looping it will produce consistent results if amendments are made to the file such as adding rows, having more candidates, correct errors for specific, etc

for x in candidate_list:
        candidate_vote_count.append((candidate.count(x)))
        candidate_percentage.append((candidate.count(x))/(total_vote)*100)

# Verify if vote counts and % votes are correct for each candidate by printing the lists:

print(candidate_vote_count)
print(candidate_percentage)

# Find the winner of the election.  This s the person with the most votes with the below function
winner = max(set(candidate), key = candidate.count)

# Find out if the winner is correct
print(winner)

# Once results are correct, print results to terminal as per the screenshot on the Python Homework ReadMe.md file

# Output Terminal
# For Loop needed to printout for candidate results, automate the process of listing each item one by one
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_vote}")
print("-----------------------------------")
for index in range(len(candidate_list)):
	print(f"{candidate_list[index]}:  {round(candidate_percentage[index],3)}00% ({candidate_vote_count[index]})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

#output to CSV - need to import sys and add the stdout & sys codes at the beginning and End  Copy the Terminal Output print section in between the sys & stdout codes.

stdoutOrigin=sys.stdout 
sys.stdout = open("PyPoll_Results.txt", "w")

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_vote}")
print("-----------------------------------")
for index in range(len(candidate_list)):
	print(f"{candidate_list[index]}:  {round(candidate_percentage[index],3)}00% ({candidate_vote_count[index]})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")
sys.stdout.close()
sys.stdout=stdoutOrigin
