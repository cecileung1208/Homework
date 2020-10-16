import os
import csv
import sys


filepath = os.path.join("Resources","Py_Poll.csv")

voter_ID = []
county = []
candidate = []

with open (filepath, 'r', encoding = 'utf-8') as pypoll_data:
    csvreader = csv.reader(pypoll_data, delimiter =",")
    header = next(csvreader, None)

    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

total_vote = (len(voter_ID))

candidate_list = list(set((candidate)))

candidate_vote_count =[]
candidate_percentage = []

for x in candidate_list:
        candidate_vote_count.append((candidate.count(x)))
        candidate_percentage.append((candidate.count(x))/(total_vote)*100)

winner = max(set(candidate), key = candidate.count)

print("Election Results")
print("-----------------------------------")
print(f"Total Votes: {total_vote}")
print("-----------------------------------")
for index in range(len(candidate_list)):
	print(f"{candidate_list[index]}:  {round(candidate_percentage[index],3)}00% ({candidate_vote_count[index]})")
print("-----------------------------------")
print(f"Winner: {winner}")
print("-----------------------------------")

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
