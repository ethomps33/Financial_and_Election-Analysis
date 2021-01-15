import csv
import os

total_votes = 0
vote_countK = 0
vote_countC = 0
vote_countL = 0
vote_countO = 0

election_data = os.path.join("Resources/election_data.csv")

with open(election_data) as csvfile:
    election_csv = csv.reader(csvfile, delimiter = ',')
    election_header = next(election_csv)
    first_row = next(election_csv)

    total_votes+=1

    for row in election_csv:
        total_votes+=1
        candidate = (''.join(row[2]))
        if candidate == 'Khan':
            vote_countK+= 1
        if candidate == 'Correy':
            vote_countC+= 1
        if candidate == 'Li':
            vote_countL+= 1
        else:
            vote_countO+= 1
            
 
        
    #print(total_votes)



    
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------")
    print(f'Khan: {vote_countK}')
    print(f'Correy: {vote_countC}')
    print(f'Li: {vote_countL}')
    print(f"O'Tooley: {vote_countO}")
    print('-------------------------')
    print(f'Winner: ')
    print('-------------------------')
