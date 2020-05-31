import io
import Appliance
from Appliance import ApplianceType



class Person():
    def __init__(self):
        self.appliance_list = []
        self.createAppliances()

    def createAppliances(self):
        data_file = open(Appliance.PATH_TO_APPLIANCE_DEFINITION,"r")
        appliance_sub_list = []
        lineCount = 0
        while True:
            lineCount += 1
            line = data_file.readline()
            if line == "":
                print("\t\t\t[Notice]: End Of File Reached")
                break
            elif lineCount == 1:
                print("\t\t\t[Notice]: Skipping first line")
            else:
                line = line.replace("\n","")
                values = line.split(",")
                new_appliance = Appliance.createAppliance(values[0],float(values[1]),float(values[3]),float(values[4]))  #(name, prob_ownership, mean_power, power_devation)
                
                if new_appliance != None:
                    on_matrix = []
                    for i in range(5,29,1):
                        on_matrix.append(float(values[i]))
                        print("\t\t\t\t\t[Notice]: Adding " + values[i] + " to on_matrix")
                    new_appliance.set_on_matrix(on_matrix)
                    appliance_sub_list.append(new_appliance)
                    print("\t\t\t\t[Notice]: Created Appliance: " + str(len(appliance_sub_list)))
        print("\t\t\t[Notice]: Created a person with " + str(len(appliance_sub_list)) + " appliances")
                    
                

person = Person()