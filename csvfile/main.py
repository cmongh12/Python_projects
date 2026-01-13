import csv

with open ("gui/csvfile/students.csv","r") as file:
    findData = csv.reader(file)
    for row in findData:
        print(row)
