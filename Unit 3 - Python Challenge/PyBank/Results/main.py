import os
import csv
import sys


filepath = os.path.join("Resources","PyBank_Resources_budget_data.csv")

date = []
pl_total = []
pl_change = []


with open (filepath, 'r', encoding = 'utf-8') as pybank_data:
    csvreader = csv.reader(pybank_data, delimiter =",")
    header = next(csvreader, None)
   
    for row in csvreader:
        date.append(row[0])
        pl_total.append(int(row[1]))

    for i in range(1,len(pl_total)):
        pl_change.append(int(pl_total[i]) - int(pl_total[i-1]))
        pl_change_avg = round(sum(pl_change)/len(pl_change),2)
        pl_change_max = max(pl_change)
        pl_change_min = min(pl_change)
        pl_change_max_date = str(date[pl_change.index(max(pl_change))])
        pl_change_min_date = str(date[pl_change.index(min(pl_change))])


print("Finanacial Summary")
print("--------------------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total:  ${sum(pl_total)}")
print(f"Average Change:  ${pl_change_avg}")
print(f"Greatest Increase in Profits:  {pl_change_max_date} $({pl_change_max})")
print(f"Greatest Decrease in Profits:  {pl_change_min_date} $({pl_change_min})")

stdoutOrigin=sys.stdout 
sys.stdout = open("Financial_Summary.txt", "w")

print("Finanacial Summary")
print("--------------------------------------------")
print(f"Total Months: {len(date)}")
print(f"Total:  ${sum(pl_total)}")
print(f"Average Change:  ${pl_change_avg}")
print(f"Greatest Increase in Profits:  {pl_change_max_date} $({pl_change_max})")
print(f"Greatest Decrease in Profits:  {pl_change_min_date} $({pl_change_min})")


sys.stdout.close()
sys.stdout=stdoutOrigin


