import csv

CUSTOMER_FILE = 'customers.csv'
NEW_FILE = 'customer_country.csv'

infile = open(CUSTOMER_FILE,'r',newline='')
reader = csv.reader(infile)
next(reader)
data = []
for row in reader:
    fname = row[1]
    lname = row[2]
    country = row[4]
    data.append([fname, lname, country])




outfile = open(NEW_FILE,'w',newline='')
writer = csv.writer(outfile)
writer.writerows(data)


