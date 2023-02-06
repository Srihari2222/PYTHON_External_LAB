# 1 (i). Write the following classes with class variables, instance variable and illustration
# the self variable
#    Robot (to greet the world).
class Robot:
    def __init__(self,name):
        self.name=name
    def greet(self):
        print(f"Robot says hello to {self.name}")


robot = Robot(input())
robot.greet()

# sample input1=sudheer
# sample output1=Robot says hello to sudheer.
#
# sample input2=kumar
# sample output2=Robot says hello to kumar.