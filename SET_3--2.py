# Given a number A which contains only digits 0's and 1's. Your task is to make
# all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0) only. If it
# is possible to make all the digits same by just flipping one digit then print
# 'YES' else print 'NO'.
x=int(input("Enter a number which contains only digits 0's and 1's: "))
y=str(x)
if y.count('0')==1 or y.count('1')==1:
    print("YES")
else:
    print("NO")

# Sample input & output 1:
# Enter a number which contains only digits 0's and 1's: 101011
# NO
#
# Sample input & output 2:
# Enter a number which contains only digits 0's and 1's: 1111101
# YES
#
# Sample input & output 3:
# Enter a number which contains only digits 0's and 1's: 0001000
# YES