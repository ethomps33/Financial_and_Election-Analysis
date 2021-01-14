import csv
import os

total_votes = 0
candidate = ['', 0]
election_data = os.path.join("Resources/election_data.csv")

with open(election_data) as csvfile:
    election_csv = csv.reader(csvfile, delimiter = ',')
    election_header = next(election_csv)
    first_row = next(election_csv)

    total_votes+=1

    for candidate in election_csv:
        total_votes+=1
        candidate+= row[2]
    print(candidate)
        
    #print(total_votes)



    
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------")
