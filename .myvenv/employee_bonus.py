import csv 

CUSTOMER_FILE = 'EmployeePay.csv'

infile = open(CUSTOMER_FILE,'r',newline='')
reader = csv.reader(infile)
next(reader)

for row in reader:
    fname = row[1]
    lname = row[2]
    salary = float(row[3])
    bonus = float(row[4])
    total = float(salary * (bonus + 1))

    print('Employee name:', fname, lname, 'Total Pay:', format(total,'>10.2f'))

    input('Press key to continue...')
