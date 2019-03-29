import csv
import os

input_file = os.path.join('.','Resources','election_data.csv')
output_file = os.path.join('.','Resources','analysis.txt')
total_vote = 0
khan_count = 0
kahn_pct = 0.0
correy_count = 0
correy_pct = 0.0
li_count = 0
li_pct = 0.0
otooley_count = 0
otooley_pct = 0.0
winner = ""
analysis_output = ""

with open(input_file, newline='') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    next(csvreader, None)
    data = list(csvreader)
    #Vote, County, Candidate
    #print(data[0])
    total_vote = len(data)
    
    for row in data: 
        if row[2] == 'Khan':
            khan_count += 1
        elif row[2] == 'Correy':
            correy_count += 1
        elif row[2] == 'Li':
            li_count += 1
        else:
            otooley_count += 1

if khan_count > correy_count:
    if khan_count > li_count:
        if khan_count >otooley_count:
            winner = "Khan"
elif correy_count > li_count:
    if correy_count > otooley_count:
        winner = "Correy"
elif li_count > otooley_count:
    winner = "Li"
else:
    winner = "O'Tooley"
    
khan_pct = format((khan_count/total_vote)*100,'.3f')
correy_pct = format((correy_count/total_vote)*100,'.3f')
li_pct = format((li_count/total_vote)*100,'.3f')
otooley_pct = format((otooley_count/total_vote)*100,'.3f')
line = '-' * 25

analysis_output = f"""Election Results
{line}
Total Votes: {total_vote}
{line}
Khan: {khan_pct}% ({khan_count})
Correy: {correy_pct}% ({correy_count})
Li: {li_pct}% ({li_count})
O'Tooley: {otooley_pct}% ({otooley_count})
{line}
Winner: {winner}
{line}"""

print(analysis_output)

with open(output_file, mode='w+') as analysis:
    analysis.write(analysis_output)