# A professor calls out student IDs of students one by one while marking
# attendance. He notices that the number of students recorded in the attendance
# sheet is far more than the number of students who are actually present in the
# classes. Hence, he decides to use a chitti the robot which can record the
# students' voices and keep track of which students have responded to attendance
# calls. At the end of each session, the robot outputs the student IDs of the
# students who have responded to attendance calls. With this information, the
# professor needs your help to find out which students were absent. Write a
# program which takes an integer array a denoting the student IDs recorded by
#the robot and print the list of student IDs of the students which were absent
# in increasing order.
n=int(input("Enter strength of class: "))
a=[int(i) for i in input("Enter attendance: ").split()]
b=[]
for j in range(1,n+1):
    if a.count(j)==0:
        b.append(j)
print("List of student IDs of the students which were absent:")
print(*b)

# Sample input & output:
#
# Enter strength of class: 10
# Enter attendance: 1 2 2 3 10 5 2 8 1 10
# List of student IDs of the students which were absent:
# 4 6 7 9