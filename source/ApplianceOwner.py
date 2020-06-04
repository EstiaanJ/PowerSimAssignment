import io
import Appliances
from pathlib import Path
from Appliances import ApplianceType
from Appliances import Appliance

class ApplianceOwner():
    def __init__(self):
        self.appliance_list = []
        self.logging: bool = False
        self.path_to_appliance_definition = Path("C:/Users/Estia/Source/VS Code/Python/FOP/Assignment/PowerSimAssignment/Data/appliance_def.csv")


    def setLogging(self,logging):
        self.logging = logging


    def setPath(self,path):
        self.path_to_appliance_definition = path

    def createAppliances(self,probability_columb_index):
        data_file = open(self.path_to_appliance_definition,"r")
        lineCount = 0
        while True:
            lineCount += 1
            line = data_file.readline()
            if line == "":
                if self.logging: 
                    print("\t\t\t[Notice]: End Of File Reached")
                break
            elif lineCount == 1:
                if self.logging: 
                    print("\t\t\t[Notice]: Skipping first line")
            else:
                line = line.replace("\n","")
                values = line.split(",")
                new_appliance = Appliances.createAppliance(values[0],float(values[probability_columb_index]),float(values[3]),float(values[4]))  #(name, prob_ownership, mean_power, power_devation)
                
                if new_appliance != None:
                    on_matrix = []
                    for i in range(5,29,1):
                        on_matrix.append(float(values[i]))
                        if self.logging: 
                            print("\t\t\t\t\t[Notice]: Adding " + values[i] + " to on_matrix")
                    new_appliance.setOnMatrix(on_matrix)
                    new_appliance.setLogging(self.setLogging)
                    self.appliance_list.append(new_appliance)
                    if self.logging: 
                        print("\t\t\t\t[Notice]: Created Appliance of type: " + new_appliance.name + " which is appliance number: " + str(len(self.appliance_list)) + " with a typical power of: " + str(new_appliance.operational_power))
        if self.logging: 
            print("\t\t\t[Notice]: Created a person with " + str(len(self.appliance_list)) + " appliances")

    def tickEnergy(self,hour_of_day) -> float:
        sum_of_energy = 0.0
        for i in self.appliance_list:
            sum_of_energy += i.tickEnergy(hour_of_day)
        return sum_of_energy


class Person(ApplianceOwner):
    def __init__(self):
        ApplianceOwner.__init__(self)
    
    def getSummary(self,person_num) -> str:
        summary = "\t\t--- Person " + str(person_num) + "'s summary--- \n"
        summary += "\t\tNo. Appliances: " + str(len(self.appliance_list)) + "\n"

        summary += "\t\t*** Summary of personal appliances: *** \n"
        for i in range(len(self.appliance_list)):
            summary += self.appliance_list[i].getSummary(i,3) + "\n"

        summary += "\t\t### End of person's summary ###\n"
        return summary
        


class HouseHold(ApplianceOwner):
    def __init__(self,number_of_people):
        ApplianceOwner.__init__(self)
        self.number_of_people = number_of_people
        self.person_list = []


    def createResidents(self):
        for i in range(self.number_of_people):
            person = Person()
            person.setLogging(self.logging)
            person.createAppliances(1)
            self.person_list.append(Person())        

    def tickEnergy(self,hour_of_day) -> float:
        sum_of_energy = super().tickEnergy(hour_of_day)
        for i in self.person_list:
            sum_of_energy += i.tickEnergy(hour_of_day)
        return sum_of_energy
    
    def getSummary(self,household_num) -> str:
        summary = "\t--- Household " + str(household_num) + " summary--- \n"
        summary += "\tNo. People: " + str(len(self.person_list)) +"\n"
        summary += "\tNo. Appliances: " + str(len(self.appliance_list)) + "\n"

        summary += "\t*** Summary of household persons: *** \n"
        for i in range(len(self.person_list)):
            summary += self.person_list[i].getSummary(i) + "\n"

        summary += "\t*** Summary of household appliances: *** \n"
        for i in range(len(self.appliance_list)):
            summary +=  self.appliance_list[i].getSummary(i,2) + "\n"
        
        summary += "\t### End of household summary ###\n"
        return summary

                

#person = Person()
#person.setLogging(True)
#person.createAppliances()