import csv

employees = open("EmployeePay.csv", "r")

employee_file = csv.reader(employees, delimiter=",")

next(employee_file)

for row in employee_file:
    totalPay = float(row[3]) + (float(row[3]) * float(row[4]))
    print(row[1], row[2], totalPay)
    input()
