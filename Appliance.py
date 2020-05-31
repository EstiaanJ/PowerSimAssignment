import numpy


#https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html



    


class Appliance():
    def __init__(self,name,on_matrix,mean_power,power_devation):
        self.name: str = name
        self.mean_power = mean_power
        self.power_devation = power_devation

    

        
class PersonalAppliance(Appliance):
    def __init__(self,name,on_matrix,mean_power,power_devation,prob_ownership):
        Appliance.__init__(self,name,on_matrix,mean_power,power_devation)
        self.prob_ownership = prob_ownership

class HouseholdAppliance(Appliance):
    def __init__(self,name,on_matrix,mean_power,power_devation,prob_ownership):
        Appliance.__init__(self,name,on_matrix,mean_power,power_devation)
        self.prob_ownership = prob_ownership

def createAppliances(path_to_appliances_definition):
    data_file = open(path_to_appliances_definition,"r")
    
    while True:
        line = data_file.readline()
        if(line == ""):
            print("[Notice]: End Of File Reached")
            break
        else:
            line = line.replace("\n","")
            #values = line.