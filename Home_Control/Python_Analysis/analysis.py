"""
This program takes in CSV values that represent inputs from a temperature sensor
and display a report indicating the data's average, minimum and maximum values
The first argument of the program is the address to the CSV file
Example Innvocation: python3 ./analysis.py feed_data.csv
"""

import sys
import csv

#Get the Temperature Values
infile = open(sys.argv[1])
reader = csv.reader(infile)
headings = []
headings = next(reader)
rows = []
for line in reader:
  rows.append(float(line[1]))

#Calculate the Average
length = len(rows)
sum = 0
for n in rows:
  sum = sum + n

#Calculate the Minimum
minu = rows[0]
for n in rows:
  if(minu > n):
    minu = n

#Calculate the Maximum
maxa = rows[0]
for n in rows:
  if(maxa < n):
    maxa = n

#Print Report
print("Printing Feed Data Report")
print("=========================")

print("Maximum Temperature: ",maxa)
print("Average Temperature: ",sum/length)
print("Minimum Temperature: ",minu)


print("=========================")
