import csv

customers = open("customers.csv", "r")

customer_file = csv.reader(customers, delimiter=",")

next(customer_file)

total = 0
for row in customer_file:
    print(row[1], row[2] + ",", row[4])
    total += 1
print(total, "total customers read")
