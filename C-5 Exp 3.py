print("Name : Aiswarya Sunil ")
print("Admission No: A24MCA004")
print("Experiment No: 17")

import csv

with open('input.csv', 'r') as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(row)
