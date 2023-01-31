import csv


SALES_FILE = 'sales.csv'
NEW_FILE = 'salesreport.csv'


infile = open(SALES_FILE,'r',newline='')
reader = csv.reader(infile)
next(reader)
data = []

for row in reader:
    cust_id = row[0]
    sub_total = float(row[3])
    tax = float(row[4])
    frieght = float(row[5])
    total = sub_total + tax + frieght
    found = False
    for i in range(len(data)):
        if data[i][0] == cust_id:
            data[i][1] += total
            found = True
    if not found:
        data.append([cust_id, total])


infile.close()



outfile = open(NEW_FILE,'w',newline='')
writer = csv.writer(outfile, delimiter= '')
writer.writerow(['Customer ID' '|    Total'])
for cust_id, total in data:
    writer.writerow([format(cust_id,'>10'), format(total,'>10.2f')])

outfile.close()



