# Write the following classes with class variables, instance variable and
# illustration the self variable
#           1 (ii). ATM (to deposit and withdraw amount from ATM machine)
class ATM:
    def __init__(self):
        self.balance=50000

    def withdraw(self,amount):
        if self.balance<amount:
            print(f"Insufficient Balance")
        else:
            self.balance-=amount
            print(f"Remaining balance : {self.balance}")
    def deposit(self,amount):
        self.balance+=amount
        return self.balance


atm=ATM()
atm.withdraw(int(input("Enter the amount to withdraw:")))
bal = atm.deposit(int(input("Enter the amount to deposit: ")))
print(f"Updated Balance {bal}")
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
