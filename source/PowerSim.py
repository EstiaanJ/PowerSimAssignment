from Community import Community
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import BooleanVar




def runSimulation(households,mean,sd,days,debug,solar):
    community = Community(households,mean,sd)
    community.setLogging(debug)
    community.setSolarPanelStatus(solar)
    community.createHouseHolds()
    totalDailyEnergyInKWH = 0
    energy_list = []

    #print(community.getSummary())

    for j in range(days):
        for i in range(24):
            energy_used_this_hour_kWh = (community.tickEnergy(i)/3600000)
            totalDailyEnergyInKWH += energy_used_this_hour_kWh
            energy_list.append(energy_used_this_hour_kWh)
        

    print(str(totalDailyEnergyInKWH) + " kWh")
    plt.plot(energy_list)
    plt.ylabel("Energy (kWh)")
    plt.xlabel("Time (hours)")
    plt.grid()
    plt.show()

def run_button():
    households = int(entry_households.get())
    mean = float(entry_people.get())
    sd = float(entry_SD.get())
    days = int(entry_days.get())
    debug = checkbox_log_state.get()
    solar = checkbox_solar_state.get()
    #TODO if days*mean*households is high, warn user this could take some time
    runSimulation(households,mean,sd,days,debug,solar)




#https://www.python-course.eu/tkinter_entry_widgets.php
#https://realpython.com/python-gui-tkinter/
main_window = tk.Tk()
main_window.title("PowerSim: Simulation Setup")
#tk.Label(main_window,text="Simulation Setup").grid(row=0,column=1)
tk.Label(main_window,text="Number of households:").grid(row=1)
tk.Label(main_window,text="Mean people per household:").grid(row=2)
tk.Label(main_window,text="Standard Deviation of people per house:").grid(row=3)
tk.Label(main_window,text="Number of days to simulate: ").grid(row=4)

entry_households = tk.Entry(main_window)
entry_people = tk.Entry(main_window)
entry_SD = tk.Entry(main_window)
entry_days = tk.Entry(main_window)

entry_households.grid(row=1,column=2)
entry_people.grid(row=2,column=2)
entry_SD.grid(row=3,column=2)
entry_days.grid(row=4,column=2)

tk.Button(main_window,text="Run",command=run_button).grid(row=5,column=1)

checkbox_log_state = BooleanVar()
checkbox_solar_state = BooleanVar()
tk.Checkbutton(main_window,text="Enable Debug Output",variable=checkbox_log_state).grid(row=5,column=0)
tk.Checkbutton(main_window,text="Enable Solar Panels",variable=checkbox_solar_state).grid(row=5,column=3)

main_window.mainloop()