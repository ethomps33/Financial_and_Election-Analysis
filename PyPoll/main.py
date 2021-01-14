import csv
import os

election_data = os.path.join("Resources/election_data.csv")

with open(election_data) as csvfile:
    election_csv = csv.reader(csvfile, delimiter = ',')
    election_header = next(election_csv)
    first_row = next(election_csv)
print(first_row)