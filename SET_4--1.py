# Write a program to print list of tuples which has a number and its cube value.
n = int(input())
lst=[]
for i in range(n):
    i=int(input())
    lst.append(i)
print(lst)
new_lst = [(i,i**3) for i in lst]
print(new_lst)

# Sample input1 and output1:
#
# 5    (Choose a number to insert no. of elements into list).
# 1
# 2
# 3
# 4
# 5
# [1, 2, 3, 4, 5]   (Print original list)
# [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125)]	    (Print list of tuples which has a number and its cube value.)
#
#
# Sample input2 and output2:
#
# 3		(Choose a number to insert no. of elements into list).
# 15
# 25
# 34
# [15, 25, 34]		(Print original list)
# [(15, 3375), (25, 15625), (34, 39304)]   (Print list of tuples which has a number and its cube value.)