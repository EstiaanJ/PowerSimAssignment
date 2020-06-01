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

class ApplianceType():
    def __init__(self,name,mean_power,power_devation):
        self.name: str = name
        self.mean_power = mean_power
        self.power_devation = power_devation
        self.on_matrix = []
        self.loging = False
    
    def setOnMatrix(self,on_matrix):
        self.on_matrix = on_matrix
    
    def setLogging(self,logging):
        self.logging = logging

class Appliance(ApplianceType):
    def __init__(self,name,mean_power,power_devation,operational_power):
        ApplianceType.__init__(self,name,mean_power,power_devation)
        self.operational_power = operational_power
    
    def isOn(self,hour_of_day) -> bool:
        rand = random.random()
        if rand < self.on_matrix[hour_of_day]:
            #print("This appliance " + self.name + " is on!")
            return True
        else:
            #print("This appliance " + self.name + " is off")
            return False
    
    def tickEnergy(self,hour_of_day) -> float:
        energy_consumed = 0.0
        if self.isOn(hour_of_day):
            energy_consumed = self.operational_power * 60.0 * 60.0 #convert from J/s to Jh
        return energy_consumed
        


#This is inspired by static factory methods from java, c# etc
def createAppliance(name, prob_ownership, mean_power, power_devation) -> Appliance:
    rand = random.random()
    return_appliance = None
    if rand < prob_ownership:
        #create new appliance
        operational_power = abs(numpy.random.randn() * power_devation + mean_power)
        return_appliance = Appliance(name,mean_power,power_devation,operational_power)
    return return_appliance
