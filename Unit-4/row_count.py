import csv

with open(r'C:\Users\Shivaji Athare\Desktop\Python Codes\2nd SEM\Class Codes\Unit- 4\data.csv', 'r') as file:
    csv_reader = csv.reader(file)
    row_count = 0
    for row in csv_reader:
        row_count += 1

print("Total number of rows:", row_count)