
from HouseHold import HouseHold
import numpy



class Community():
    def __init__(self,number_of_households,mean_residents,sd_residents):
        self.number_of_households = number_of_households
        self.mean_residents = mean_residents
        self.sd_residents = sd_residents
        self.household_list = []
        print("[Notice]: Created community with " + str(number_of_households) + " households")

        for i in range(number_of_households): 
            #https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html
            num_residents = int(numpy.random.randn() * sd_residents + mean_residents) #https://www.science-emergence.com/Articles/Create-random-numbers-from-a-normal-distribution-with-numpy-in-python-/
            if num_residents < 1: #A household cannot have less than 1 resident. This kind of breaks the normal distribution, but I think that's okay.
                num_residents = 1 #I don't think the number of people per household is a normal distribution anyway, but that is beyond the scope of this unit.
            self.household_list.append(HouseHold(num_residents))
            print("\t[Notice]: Created a household with " + str(num_residents) + " resident(s)")

community = Community(3,3.2,1.5)