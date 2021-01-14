import os
import csv

budget_data = os.path.join('Resources', 'budget_data.csv')
row_count = 0
total_sum = 0
total_change = 0
largest_increase = 0
largest_decrease = 0

with open(budget_data) as csvfile:
    budget_csv = csv.reader(csvfile, delimiter = ',')
    budget_header = next(budget_csv)
    first_row=next(budget_csv)
    last_month_val= int(first_row[1])
    row_count+=1


    for row in budget_csv:
        row_count+=1
        increase_date = row
        decrease_date = row

        monthly_change= int(row[1]) - last_month_val
        
        total_change += monthly_change
        total_sum+=int(row[1])
        last_month_val = int(row[1])
        
        largest_increase = max(largest_increase, monthly_change)
        increase_date= row[0]
        largest_decrease = min(largest_decrease, monthly_change)

        
            
        
    
    print("Finacial Analysis")
    print("--------------------------------")
    print(f'Total Months: {row_count}')
    print(f'Total: ${total_sum}')
    print(f'Average Change: ${round((total_change/row_count), 2)}')
    print(f'Greatest Increase in Profits: \n {increase_date}  ${largest_increase} ')
    print(f'Greatest Decrease in Profits: \n  ${largest_decrease}') 

        
