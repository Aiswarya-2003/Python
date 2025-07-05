import csv
print("Name : Aiswarya Sunil ")
print("Admission No: A24MCA004")
print("Experiment No: 18")

columns_to_read = [0, 2]
with open('input.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print([row[i] for i in columns_to_read])
