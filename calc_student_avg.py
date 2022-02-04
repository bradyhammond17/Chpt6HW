import csv

students = open("Student_Scores.csv", "r")

student_file = csv.reader(students, delimiter=",")

outfile = open("student_avg.csv", "w")

next(student_file)

for row in student_file:
    avg = (int(row[1]) + int(row[2]) + int(row[3])) / 3
    studentAvg = row[0] + "," + str(float(avg))
    outfile.write(studentAvg + "\n")
outfile.close()
