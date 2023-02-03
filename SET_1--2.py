# Write the following classes with class variables, instance variable and
# illustration the self variable
#           1 (ii). ATM (to deposit and withdraw amount from ATM machine)
class ATM:
    def __init__(self):
        self.amount = 50000

    def w(self):
        withdraw = int(input("Enter the amount to withdraw: "))
        if self.amount < withdraw:
            print(f"Insufficient balance")
        else:
            self.amount = self.amount - withdraw
            print(f"Remaining balance: {self.amount}")

    def d(self):
        deposit = int(input("Enter the amount to deposit: "))
        self.amount = self.amount + deposit
        print(f"Updated balance: {self.amount}")


atm = ATM()
atm.w()
atm.d()

# Sample input1 & output1:
#
# Enter the amount to withdraw: 9500
# Remaining balance:  40500
# Enter the amount to deposit: 2800
# Updated balance:  43300
#
# Sample input2 & output2:
#
# Enter the amount to withdraw: 55000
# Insufficient Balance
# Enter the amount to deposit: 4500
# Updated balance:  54500
