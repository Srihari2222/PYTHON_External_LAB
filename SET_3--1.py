# Given a positive integer 'x' (with even number of digits in it), compute the
# difference between the sum of the digits occurring in the alternate positions
# (starting from the first position) and the sum of the digits occurring in the
# alternate positions, starting from the last rightmost position of 'x'.
x=int(input("Enter an integer: "))
y=str(x)
c=0
d=0
if len(y)%2!=0 or x<0:
    print("Invalid number")
else:
    for i in y[::2]:
        c=c+int(i)
    for j in y[1::2]:
        d=d+int(j)
    print(f"Difference between the sums of the digits occurring in the alternate positions: {abs(c-d)}")

# Sample input & output 1:
# Enter an integer: 152
# Invalid number
#
# Sample input & output 2:
# Enter an integer: -25
# Invalid number
#
# Sample input & output 3:
# Enter an integer: 12345678
# Difference between the sums of the digits occurring in the alternate positions: 4
