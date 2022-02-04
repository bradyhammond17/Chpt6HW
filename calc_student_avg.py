import csv

students = open("Student_Scores.csv", "r")

student_file = csv.reader(students, delimiter=",")

next(student_file)

for row in student_file:
    avg = (int(row[1]) + int(row[2]) + int(row[3])) / 3
    prin
