import numpy
from pathlib import Path
import io
import random



PATH_TO_APPLIANCE_DEFINITION: str = Path("PowerSimAssignment/Data/appliance_def.csv") #https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

#I battled with deciding how to code the path for the appliance file.
#I don't like hard-coding it, but I see two alternatives:
#1) Would be to have it as a global variable in the "main" file, the one that is executed. Doing this would mean that this Person class is no longer
#as portable, and to use it, by itself, in another program would require significant refactoring. Plus, changes to the main file could break this class
# in general, less portable, more interconnected classes are considered bad practice in OOP design
#2) Would be to have the path passed down from the owner object to the owned object via each new object's constructor, so Community -> HouseHold -> Person
#but this adds an import all the way down that path which is only relevant to the Person and Household classes, not very ellogant either.

f = open(PATH_TO_APPLIANCE_DEFINITION,"r")
print(f.readline())

class Appliance():
    def __init__(self,name,mean_power,power_devation):
        self.name: str = name
        self.mean_power = mean_power
        self.power_devation = power_devation
        self.on_matrix = []
    
    def set_on_matrix(self,on_matrix):
        self.on_matrix = on_matrix


#This is inspired by static factory methods from java, c# etc
def createAppliance(name, prob_ownership, mean_power, power_devation) -> Appliance:
    rand = random.random()
    return_appliance = None
    if rand < prob_ownership:
        #create new appliance
        return_appliance = Appliance(name,mean_power,power_devation)
    return return_appliance
