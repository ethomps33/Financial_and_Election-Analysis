import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')
row_count = 0
total_sum = 0
total_change = 0
last_month_val = 0
greatest_increase_difference = 0
greatest_decrease_difference = 0
greatest_increase_month = 0
greatest_decrease_month = 0

with open(budget_data, 'r') as csvfile:
    budget_csv = csv.reader(csvfile, delimiter = ',')
    
    first_row=next(budget_csv)

    for row in budget_csv:
        
        if row_count != 0:
            total_change = total_change + int(row[1]) - last_month_val
        row_count+=1
        monthly_change= int(row[1]) - last_month_val
        if (monthly_change > greatest_increase_difference):
            greatest_increase_difference = monthly_change
            greatest_increase_month = row[0]

        if (monthly_change < greatest_decrease_difference):
            greatest_decrease_difference = monthly_change
            greatest_decrease_month = row[0]

        last_month_val= int(row[1])
       
        total_sum+=int(row[1])        
output_path = os.path.join("Analysis", "output_PyBank.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=":")
    csvwriter.writerow(["Finacial Analysis"])
    csvwriter.writerow(["--------------------------------"])
    csvwriter.writerow([f'Total Months: {row_count}'])
    csvwriter.writerow([f'Total: ${total_sum}'])
    csvwriter.writerow([f'Average Change: ${round((total_change/(row_count-1)), 2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: \n {greatest_increase_month} (${greatest_increase_difference})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: \n {greatest_decrease_month} (${greatest_decrease_difference})'])
    print("Finacial Analysis")
    print("--------------------------------")
    print(f'Total Months: {row_count}')
    print(f'Total: ${total_sum}')
    print(f'Average Change: ${round((total_change/(row_count-1)), 2)}')
    print(f'Greatest Increase in Profits: \n {greatest_increase_month} (${greatest_increase_difference})')
    print(f'Greatest Decrease in Profits: \n {greatest_decrease_month} (${greatest_decrease_difference})') 

        
