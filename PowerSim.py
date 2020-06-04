from Community import Community
import matplotlib.pyplot as plt
import tkinter as tk

#https://www.python-course.eu/tkinter_entry_widgets.php
#https://realpython.com/python-gui-tkinter/
main_window = tk.Tk()
main_window.title("PowerSim: Simulation Setup")
#tk.Label(main_window,text="Simulation Setup").grid(row=0)
tk.Label(main_window,text="Number of households:").grid(row=1)
tk.Label(main_window,text="Mean people per household:").grid(row=2)
tk.Label(main_window,text="Standard Deviation of people per house:").grid(row=3)
tk.Label(main_window,text="Number of days to simulate:").grid(row=4)

entry_households = tk.Entry(main_window)
entry_people = tk.Entry(main_window)
entry_SD = tk.Entry(main_window)
entry_days = tk.Entry(main_window)

entry_households.grid(row=1,column=1)
entry_people.grid(row=2,column=1)
entry_SD.grid(row=3,column=1)
entry_days.grid(row=4,column=1)

main_window.mainloop()

def runSimulation():
    community = Community(1000,2.5,0.1)
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
    plt.ylabel("Energy (kWh)")
    plt.xlabel("Time (hours)")
    plt.grid()
    plt.show()