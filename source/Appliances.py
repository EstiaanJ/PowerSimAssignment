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

class Appliance():
    def __init__(self,name,mean_power,power_devation,operational_power):
        self.name: str = name
        self.mean_power: float = mean_power
        self.power_devation: float = power_devation
        self.on_matrix: float = []
        self.loging: bool = False
        self.operational_power: float = operational_power

    def isOn(self,hour_of_day: int) -> bool:
        rand = random.random()
        if rand < self.on_matrix[hour_of_day]:
            #print("This appliance " + self.name + " is on!")
            return True
        else:
            #print("This appliance " + self.name + " is off")
            return False

    def getSummary(self,appliance_num: int,indent_num: int) -> str:
        if indent_num == 2:
            summary = "\t\t--- Appliance " + str(appliance_num) + " summary--- \n"
            summary += "\t\tAppliance Type: " + self.name + "\n"
            summary += "\t\tMean power of a " + self.name + ": " + str(self.mean_power) + " W\n"
            summary += "\t\tStandard Deviation of the power, of a " + self.name + ": " + str(self.power_devation) + " W\n"
            summary += "\t\tThis appliance's typical power: " + str(self.operational_power) + " W\n"
            summary += "\t\t### End of appliance's summary ###\n"
        else:
            summary = "\t\t\t--- Appliance " + str(appliance_num) + " summary--- \n"
            summary += "\t\t\tAppliance Type: " + self.name + "\n"
            summary += "\t\t\tMean power of a " + self.name + ": " + str(self.mean_power) + " W\n"
            summary += "\t\t\tStandard Deviation of the power, of a " + self.name + ": " + str(self.power_devation) + " W\n"
            summary += "\t\t\tThis appliance's typical power: " + str(self.operational_power) + " W\n"
            summary += "\t\t\t### End of appliance's summary ###\n"
        return summary 

    def setOnMatrix(self,on_matrix):
        self.on_matrix = on_matrix
    
    def setLogging(self,logging: bool):
        self.logging = logging

    def tickEnergy(self,hour_of_day: int) -> float:
        energy_consumed = 0.0
        if self.isOn(hour_of_day):
            energy_consumed = self.operational_power * 3600.0 #Convert from J/s to Jh TODO: This is wrong, should be 217000
        return energy_consumed

class SolarPannel(Appliance):
    pass
        


#This is inspired by static factory methods from java, c# etc
def createAppliance(name, prob_ownership, mean_power, power_devation) -> Appliance:
    rand = random.random()
    return_appliance = None
    if rand < prob_ownership:
        #create new appliance
        operational_power = abs(numpy.random.randn() * power_devation + mean_power)
        return_appliance = Appliance(name,mean_power,power_devation,operational_power)
    return return_appliance
