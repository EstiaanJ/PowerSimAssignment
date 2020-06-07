
from ApplianceOwner import ApplianceOwner
from ApplianceOwner import HouseHold
import numpy



class Community():
    def __init__(self,number_of_households,mean_residents,sd_residents):
        self.number_of_households: int = number_of_households
        self.mean_residents: float = mean_residents
        self.sd_residents: float = sd_residents
        self.household_list: ApplianceOwner = []
        self.logging: bool = False
        self.solar_panel_status = False

    #Not sure if this is technically an accessor method or more like a toString() method from java, had to make a call.
    def getSummary(self) -> str:
        summary = "--- Summary of community ---\n"
        summary += "Households: " + str(len(self.household_list)) + "\n"
        summary += "*** Summary of Households *** \n"
        for i in range(len(self.household_list)):
            summary += self.household_list[i].getSummary(i) + "\n"
        
        summary += "### End of community summary ###\n"

        return summary

    def setLogging(self,logging: bool):
        self.logging = logging 
        
        #Printing out statements can take a long time, especially if it's being done in a for loop, within a for loop, within a for loop and so on. Checking a boolean statment is much quicker
        #This also allows me to turn logging off and on without having to go through all my code and commeting out the logging statments
        #Also, this isn't technically being logged, just printed, but you get the point

    def setSolarPanelStatus(self, status: bool):
        self.solar_panel_status = status

    def createHouseHolds(self):
        for i in range(self.number_of_households): 
            #https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html
            num_residents = int(numpy.random.randn() * self.sd_residents + self.mean_residents) #https://www.science-emergence.com/Articles/Create-random-numbers-from-a-normal-distribution-with-numpy-in-python-/
            if num_residents < 1: #A household cannot have less than 1 resident. This kind of breaks the normal distribution, but I think that's okay.
                num_residents = 1 #I don't think the number of people per household is a normal distribution anyway, but that is beyond the scope of this unit.
            house_hold = HouseHold(num_residents)
            house_hold.setLogging(self.logging)
            house_hold.setSolarPanelStatus(self.solar_panel_status)
            house_hold.createResidents()
            house_hold.createAppliances(2)
            self.household_list.append(house_hold)
            if self.logging:
                print("\t[Notice]: Created a household with " + str(num_residents) + " resident(s)")
        if self.logging:
            print("[Notice]: Created community with " + str(self.number_of_households) + " households")

    def tickEnergy(self,hour_of_day: int) -> float:
        print("----------For hour: " + str(hour_of_day) + " ------------------")
        sum_of_energy = 0.0
        for i in self.household_list:
            sum_of_energy += i.tickEnergy(hour_of_day)
        print("Community: " + " consumed: " + str(sum_of_energy/3600000) + " kWh at: " + str(hour_of_day))
        print("_____________________________")
        print()
        return sum_of_energy
    
#    def simulateDailyEnergyUse(self): #In Joules
#        #TODO: Reset On_Grid
#        energy_list = []
#        for i in range(24):
#            energy_used_this_hour = self.tickEnergy(i)
#            energy_list.append(energy_used_this_hour)
#        return energy_list

#    def simulateDailyEnergyUsekWh(self) -> float:
#        energy_list = self.simulateDailyEnergyUse()
#        for i in energy_list:
#            i = i/36000000.0 #Converstion scalar for Joules to kWh
#        return energy_list
        
        
    

#community = Community(2,3.2,1.5)
#community.setLogging(False)
#community.createHouseHolds()
#print(community.getSummary())
#print(str(community.tickEnergy(5)/1000/1000))