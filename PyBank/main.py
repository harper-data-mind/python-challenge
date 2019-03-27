import csv
import os

input_file = os.path.join('.','Resources','budget_data.csv')
output_file = os.path.join('.', 'Resources','analysis.txt')
months_count = 0
net_change = 0.0
net_prof_loss = 0
great_profit = 0
profit_date = ''
great_loss = 0
loss_date = ''
i = 0

with open(input_file, newline='') as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    header = next(csvreader, None)
    data = list(csvreader)
    
    months_count = len(data)
    
    for row in data:
        net_prof_loss += (int(row[1]))
    
    while i < len(data)-1:
        change = (float(data[i+1][1]) - float(data[i][1]))
        net_change += change
        if change > great_profit:
            great_profit = int(change)
            profit_date = data[i+1][0]
        if change < great_loss:
            great_loss = int(change)
            loss_date = data[i+1][0]
        i += 1
    
avg_net = round(net_change/(months_count-1),2)    
line = "-" * 28
analysis_output = f"""Financial Analysis
{line}
Total Months: {months_count}
Total: ${net_prof_loss}
Average Change: ${avg_net}
Greatest Increase In Profits: {profit_date} (${great_profit})
Greatest Decrease In Profits: {loss_date} (${great_loss})"""

with open(output_file, mode='w+') as analysis:
    analysis.write(analysis_output)

print(analysis_output)