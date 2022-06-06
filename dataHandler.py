from cgi import test
import csv
from entry import Entry

with open('mockData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    entryList = []

    for row in csv_reader:
        if line_count ==0:
            line_count += 1

        else:
            entry = Entry(row[0],row[1],row[2],row[3],row[4])
            entryList.append(entry)
            line_count += 1

            
    
            

