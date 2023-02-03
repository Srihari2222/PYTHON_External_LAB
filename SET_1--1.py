# 1 (i). Write the following classes with class variables, instance variable and illustration
# the self variable
#    Robot (to greet the world).
class Robot:
    def __init__(self,name):
        self.name=name
a=Robot(input())
print("Robot says hello to ",a.name)

# sample input1=sudheer
# sample output1=Robot says hello to sudheer.
#
# sample input2=kumar
# sample output2=Robot says hello to kumar.