from Community import Community
import matplotlib.pyplot as plt

community = Community(1000,4,0.1)
community.setLogging(False)
community.createHouseHolds()
#print(str(community.tickEnergy(5)/1000/1000))
totalDailyEnergyInKWH = 0
energy_list = []

for j in range(3):
    for i in range(24):
        energy_used_this_hour = (community.tickEnergy(i)/(1000 * 1000))
        totalDailyEnergyInKWH += energy_used_this_hour
        energy_list.append(energy_used_this_hour)
    

print(str(totalDailyEnergyInKWH) + " kWh")
plt.plot(energy_list)
plt.show()