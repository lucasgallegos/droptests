import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import math



# Do the following in Terminal with a Roscore Running
# $rostopic echo -b <name>.bag -p /wrench > <name>.csv

rtd = 180/math.pi

data1 = pd.read_csv("hebi_drop3.csv") #reads the data from the csv file
data2 = pd.read_csv("ur3_angles_drop4_kalman.csv")

time = data1["%time"]-(data1["%time"][0]) #Pulls and normalizes the data to start from t=0

angle1_hebi = data1["field.Angle1"] #See pandas documentation on how to pull data 
angle2_hebi = data1["field.Angle2"]
angle3_hebi = data1["field.Angle3"]

angle4_hebi = data1["field.Angle4"]
angle5_hebi = data1["field.Angle5"]
angle6_hebi = data1["field.Angle6"]

time = time.values #converts to np array

print(time)

angle1_hebi = angle1_hebi.values
angle2_hebi = angle2_hebi.values
angle3_hebi = angle3_hebi.values

angle4_hebi = angle4_hebi.values
angle5_hebi = angle5_hebi.values
angle6_hebi = angle6_hebi.values

#ur3

time_ur3 = data2["%time"]-(data2["%time"][0])

angle1_ur3 = data2["field.Angle1"] #See pandas documentation on how to pull data 
angle2_ur3 = data2["field.Angle2"]
angle3_ur3 = data2["field.Angle3"]

angle4_ur3 = data2["field.Angle4"]
angle5_ur3 = data2["field.Angle5"]
angle6_ur3 = data2["field.Angle6"]

time_ur3 = time_ur3.values #converts to np array

angle1_ur3 = angle1_ur3.values
angle2_ur3 = angle2_ur3.values
angle3_ur3 = angle3_ur3.values

angle4_ur3 = angle4_ur3.values
angle5_ur3 = angle5_ur3.values
angle6_ur3 = angle6_ur3.values




#Forces
plt.subplot(6,2,1)
plt.plot(time,-angle1_hebi*rtd-19, label='Series Elastic Robot')
plt.plot(time_ur3-1.5e9,-angle1_ur3*rtd-10, label='Rigid UR3 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 1 [deg]')
plt.xlim(0,0.8e10)
plt.title('Haptic Feedback Device - Dynamic Response',fontsize=16)

plt.subplot(6,2,3)
plt.plot(time,angle2_hebi*rtd+25, label='Series Elastic Robot')
plt.plot(time_ur3-1.5e9,angle2_ur3*rtd, label='Rigid UR3 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 2 [deg]')
plt.xlim(0,0.8e10)


plt.subplot(6,2,5)
plt.plot(time,-angle3_hebi*rtd-25, label='Series Elastic Robot')
plt.plot(time_ur3-1.5e9,-angle3_ur3*rtd, label='Rigid UR3 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 3 [deg]')
plt.xlim(0,0.8e10)


plt.subplot(6,2,7)
plt.plot(time,angle4_hebi*rtd-10, label='Series Elastic Robot')
plt.plot(time_ur3-1.5e9,angle4_ur3*rtd, label='Rigid UR3 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 4 [deg]')
plt.xlim(0,0.8e10)
#plt.title('Torque')

plt.subplot(6,2,9)
plt.plot(time,-angle5_hebi*rtd+5, label='Series Elastic Robot')
plt.plot(time_ur3-1.5e9,-angle5_ur3*rtd-5, label='Rigid UR3 Robot')
plt.legend()
#plt.xlabel('time [s]')
plt.ylabel('Angle 5 [deg]')
plt.xlim(0,0.8e10)


plt.subplot(6,2,11)
plt.plot(time,angle6_hebi*rtd+17, label='Series Elastic Robot')
plt.plot(time_ur3-1.5e9,angle6_ur3*rtd, label='Rigid UR3 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 6 [deg]')
plt.xlim(0,0.8e10)

plt.show()


