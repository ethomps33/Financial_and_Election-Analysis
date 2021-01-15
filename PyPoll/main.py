#import dependancies
import csv
import os

#setting looping variable
total_votes = 0
vote_countK = 0
vote_countC = 0
vote_countL = 0
vote_countO = 0

#Opening the file through the file path
election_data = os.path.join("Resources/election_data.csv")

with open(election_data, 'r') as csvfile:
    election_csv = csv.reader(csvfile, delimiter = ',')
    election_header = next(election_csv)
    first_row = next(election_csv)

    #Creating a loop to loop through the candidates to total the votes and set a percent
    for row in election_csv:
        total_votes+=1
        candidate = (''.join(row[2]))
        if candidate == 'Khan':
            vote_countK+= 1
            k_percent = vote_countK/total_votes
        if candidate == 'Correy':
            vote_countC+= 1
            c_percent = vote_countC/total_votes
        if candidate == 'Li':
            vote_countL+= 1
            l_percent = vote_countL/total_votes
        if candidate == "O'Tooley":
            vote_countO+= 1
            o_percent = vote_countO/total_votes
        


    #Output
    print("Election Results")
    print("------------------------")
    print(f'Total Votes: {total_votes}')
    print("------------------------")
    print(f'Khan: {round((k_percent*100),1)}% {vote_countK}')
    print(f'Correy: {round((c_percent*100),1)}% {vote_countC}')
    print(f'Li: {round((l_percent*100),1)}% {vote_countL}')
    print(f"O'Tooley: {round((o_percent*100),1)}% {vote_countO}")
    print('-------------------------')
    print(f'Winner: Khan ')
    print('-------------------------')
output_path = os.path.join("Analysis", "output_PyPoll.csv")
with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------"])
    csvwriter.writerow([f'Total Votes: {total_votes}'])
    csvwriter.writerow(["------------------------"])
    csvwriter.writerow([f'Khan: {round((k_percent*100),1)}% {vote_countK}'])
    csvwriter.writerow([f'Correy: {round((c_percent*100),1)}% {vote_countC}'])
    csvwriter.writerow([f'Li: {round((l_percent*100),1)}% {vote_countL}'])
    csvwriter.writerow([f"O'Tooley: {round((o_percent*100),1)}% {vote_countO}"])
    csvwriter.writerow(['-------------------------'])
    csvwriter.writerow([f'Winner: Khan '])
    csvwriter.writerow(['-------------------------'])