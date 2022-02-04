import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")
outfile = open("customer_country.csv", "w")
next(customer_file)

total = 0
for row in customer_file:
    customerInfo = row[1] + "," + row[2] + "," + row[4]
    outfile.write(customerInfo + "\n")
    total += 1
print(total, "total customers read")

outfile.close()
