# Write a program to check whether the given number is Consecutive Four Sum
# Number or not. Consecutive Four Sum Number: A positive integer is called as a
# ‘Consecutive Four Sum (CFS) number’ if that number can be expressed as the sum
# of four consecutive positive integers.
n=int(input("Enter an Integer: "))
i= (n//4)-1
if 4*i+6==n:
    print(str(n) + " is Consecutive Four Sum Number")
else:
    print(f"{n} is not Consecutive Four Sum Number")

# Sample input & output 1:
# Enter an integer: 50
# 50 is Consecutive Four Sum Number
#
# Sample input & output 2:
# Enter an integer: 17
# 17	is not Consecutive Four Sum Number
