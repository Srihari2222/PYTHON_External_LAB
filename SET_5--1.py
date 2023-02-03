# Let us assume paper as the plane and a letter as a curve on the plane, then
# each letter divides the plane into regions. For example letters "A", "D", "O",
# "P", "R" divide the plane into two regions so we say these letters each have
# one hole. Similarly, letter "B" has two holes and letters such as "C", "E",
# "F", "K" have no holes. We say that the number of holes in the text is equal
# to the total number of holes in the letters of the text. Write a program to
# determine how many holes are in a given text.
str=input("Enter string: ")
count=0
for i in str:
    if i in "ADOPQR":
        count+=1
    elif i=="B":
        count+=2
print("Number of holes in given text:",count)

# Sample input & output:
#
# Enter string: HELLO STUDENTS
# Number of holes in given text: 2