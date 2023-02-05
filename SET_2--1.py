# Make a class called Restaurant. The __init__() method for Restaurant should
# store two attributes: a restaurant_name and a cuisine_type. Make a method called
# describe_restaurant() that prints these two pieces of information, and a method
# called open_restaurant() that prints a message indicating that the restaurant is
# open. Create three different instances from the class, print the two attributes
# individually, and then call both methods for each instance.
from datetime import datetime
class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}")
        print(self.cuisine_type)
    def open_restaurant(self):
        time = datetime.now().hour
        if time>=11 and time<=23:print("Restaurant Open")
        else:print("Restaurant Closed")


a=input("Enter the Restaurant Name: ")
b=input("Enter the Cuisine: ")
R=Restaurant(a,b)
R.describe_restaurant()
R.open_restaurant()

# Sample input & output 1:
# Enter the Restaurant name: Minerva
# Enter the Cuisine: South Indian Cuisine
# Welcome to Minerva
# South Indian Cuisine
# Restaurant Open
#
# Sample input & output 2:
# Enter the Restaurant name: Paradise
# Enter the Cuisine: Indian Cuisine
# Welcome to Paradise
# Indian Cuisine
# Restaurant Closed
