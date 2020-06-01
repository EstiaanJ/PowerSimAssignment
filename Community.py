
from HouseHold import HouseHold
import numpy



class Community():
    def __init__(self,number_of_households,mean_residents,sd_residents):
        self.number_of_households = number_of_households
        self.mean_residents = mean_residents
        self.sd_residents = sd_residents
        self.household_list = []
        self.logging = False

    def setLogging(self,logging):
        self.logging = logging 
        
        #Printing out statements can take a long time, especially if it's being done in a for loop, within a for loop, within a for loop and so on. Checking a boolean statment is much quicker
        #This also allows me to turn logging off and on without having to go through all my code and commeting out the logging statments
        #Also, this isn't technically being logged, just printed, but you get the point

    def createHouseHolds(self):
        for i in range(self.number_of_households): 
            #https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html
            num_residents = int(numpy.random.randn() * self.sd_residents + self.mean_residents) #https://www.science-emergence.com/Articles/Create-random-numbers-from-a-normal-distribution-with-numpy-in-python-/
            if num_residents < 1: #A household cannot have less than 1 resident. This kind of breaks the normal distribution, but I think that's okay.
                num_residents = 1 #I don't think the number of people per household is a normal distribution anyway, but that is beyond the scope of this unit.
            house_hold = HouseHold(num_residents)
            house_hold.setLogging(self.logging)
            house_hold.createResidents()
            house_hold.createAppliances()
            self.household_list.append(house_hold)
            if self.logging:
                print("\t[Notice]: Created a household with " + str(num_residents) + " resident(s)")
        if self.logging:
            print("[Notice]: Created community with " + str(self.number_of_households) + " households")


community = Community(3,3.2,1.5)
community.setLogging(True)
community.createHouseHolds()