import numpy
import matplotlib.pyplot as plt

#https://docs.scipy.org/doc/numpy-1.15.1/reference/generated/numpy.random.randn.html
mean = 3
SD = 1

data = numpy.random.randn() * SD + mean

plt.hist(data,bins=50,color="lightblue")
plt.show()
class Appliance():
    def __init__(self,name,power_rating_deviation,power_rating_mean):
        self.name: str = name
        self.power_rating_deviation = power_rating_deviation
        self.power_rating_mean = power_rating_mean
        self.power_typical = numpy.random.randn() * SD + mean

        
class PersonalAppliance(Appliance):
    pass