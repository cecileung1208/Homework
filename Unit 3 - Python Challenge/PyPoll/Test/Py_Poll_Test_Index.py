import os
import csv

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

# Quick way to get the results if vote counts are correct for each candidate
candidate_results = ([[x,candidate.count(x)] for x in set(candidate)])
print(candidate_results)

#get unique list
candidate_list = list(set(candidate))
print(candidate_list)
print(len(candidate_list))

#find out # of candidates by:
    #print(len(candidate_list)) and print to terminal and the answer is 4
# candidate_list =  [O'Tooley, Khan, Li, Correy] where index [0,1,2,3] respectively of the list
#since I have unique valuees of the list, I can count # of votes and % for each candidate
    # I need to count 4 times for each candidate & another 4 times to get the % of votes for each candidate

count_0 = candidate.count(candidate_list[0])
count_1 = candidate.count(candidate_list[1])
count_2 = candidate.count(candidate_list[2])
count_3 = candidate.count(candidate_list[3])

percent_0 = round(count_0/len(voter_ID)*100,3)
percent_1 = round(count_1/len(voter_ID)*100,3)
percent_2 = round(count_2/len(voter_ID)*100,3)
percent_3 = round(count_3/len(voter_ID)*100,3)

#find the winner with the most # of votes with the below function
winner = max(set(candidate), key = candidate.count)

#Output to Terminal as per Homework Instructions
print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {len(voter_ID)}")
print("-----------------------------------")
print(f"{candidate_list[0]}: {percent_0}00% ({count_0})")
print(f"{candidate_list[1]}: {percent_1}00% ({count_1})")
print(f"{candidate_list[2]}: {percent_2}00% ({count_2})")
print(f"{candidate_list[3]}: {percent_3}00% ({count_3})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")
