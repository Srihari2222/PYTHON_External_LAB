# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this
# value. If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps
# calling collatz() on that number until the function returns the value 1.
# Input Validation: Add try and except statements to detect whether the user
# types in a non-integer string. In the except clause, print a message to the
# user saying they must enter an integer.
def collatz(num):
    while (num != 1):
        if num % 2 == 0:
            num = num // 2
            print(num, end=' ')
        elif num % 2 != 0:
            num = num * 3 + 1
            print(num, end=' ')


try:
    num = int(input("Enter a number: "))
    collatz(num)
except:
    print("Please enter a valid INTEGER")

# Sample input & output 1:
#
# Enter a number: 3
# 10 5 16 8 4 2 1
#
# Sample input & output 2:
#
# Enter a number: hello
# Please enter a valid INTEGER
