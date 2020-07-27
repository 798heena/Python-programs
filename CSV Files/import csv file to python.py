#Python program to demonstrate how to import csv file to python

import csv
with open ('Book1.csv') as csvfile:
    read_csv = csv.reader(csvfile,delimiter=',')
    print(read_csv)
    for row in read_csv:
        print(row)