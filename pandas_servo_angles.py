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
data3 = pd.read_csv("angles_drop2_sia5_corrected.csv")

time = data1["%time"]-(data1["%time"][0]) #Pulls and normalizes the data to start from t=0
time = (time.values)/1e9 #converts to np array


angle1_hebi = data1["field.Angle1"] #See pandas documentation on how to pull data 
angle2_hebi = data1["field.Angle2"]
angle3_hebi = data1["field.Angle3"]

angle4_hebi = data1["field.Angle4"]
angle5_hebi = data1["field.Angle5"]
angle6_hebi = data1["field.Angle6"]

angle1_hebi = angle1_hebi.values
angle2_hebi = angle2_hebi.values
angle3_hebi = angle3_hebi.values

angle4_hebi = angle4_hebi.values
angle5_hebi = angle5_hebi.values
angle6_hebi = angle6_hebi.values

#ur3

time_ur3 = data2["%time"]-(data2["%time"][0])
time_ur3 = (time_ur3.values)/1e9 #converts to np array

angle1_ur3 = data2["field.Angle1"] #See pandas documentation on how to pull data 
angle2_ur3 = data2["field.Angle2"]
angle3_ur3 = data2["field.Angle3"]

angle4_ur3 = data2["field.Angle4"]
angle5_ur3 = data2["field.Angle5"]
angle6_ur3 = data2["field.Angle6"]

angle1_ur3 = angle1_ur3.values
angle2_ur3 = angle2_ur3.values
angle3_ur3 = angle3_ur3.values

angle4_ur3 = angle4_ur3.values
angle5_ur3 = angle5_ur3.values
angle6_ur3 = angle6_ur3.values

#sia5

time_sia5 = data3["%time"]-(data3["%time"][0]) #Pulls and normalizes the data to start from t=0
time_sia5 = (time_sia5.values)/1e9 #converts to np array


angle1_sia5 = data3["field.Angle1"] #See pandas documentation on how to pull data 
angle2_sia5 = data3["field.Angle2"]
angle3_sia5 = data3["field.Angle3"]

angle4_sia5 = data3["field.Angle4"]
angle5_sia5 = data3["field.Angle5"]
angle6_sia5 = data3["field.Angle6"]

angle1_sia5 = angle1_sia5.values
angle2_sia5 = angle2_sia5.values
angle3_sia5 = angle3_sia5.values

angle4_sia5 = angle4_sia5.values
angle5_sia5 = angle5_sia5.values
angle6_sia5 = angle6_sia5.values




#Forces
plt.subplot(6,2,1)
plt.plot(time,-angle1_hebi*rtd-19, label='Series Elastic Robot')
plt.plot(time_ur3-1.5,-angle1_ur3*rtd-10, label='Rigid UR3 Robot')
plt.plot(time_sia5-1.7,-angle1_sia5*rtd+40, label='Rigid SIA5 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 1 [deg]')
plt.xlim(0,5)
#plt.title('Haptic Feedback Device - Dynamic Response',fontsize=16)

plt.subplot(6,2,3)
plt.plot(time,angle2_hebi*rtd+25, label='Series Elastic Robot')
plt.plot(time_ur3-1.5,angle2_ur3*rtd, label='Rigid UR3 Robot')
plt.plot(time_sia5-1.7,angle2_sia5*rtd+40, label='Rigid SIA5 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 2 [deg]')
plt.xlim(0,5)


plt.subplot(6,2,5)
plt.plot(time,-angle3_hebi*rtd-25, label='Series Elastic Robot')
plt.plot(time_ur3-1.5,-angle3_ur3*rtd, label='Rigid UR3 Robot')
plt.plot(time_sia5-1.7,-angle3_sia5*rtd-28, label='Rigid SIA5 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 3 [deg]')
plt.xlim(0,5)


plt.subplot(6,2,7)
plt.plot(time,angle4_hebi*rtd-10, label='Series Elastic Robot')
plt.plot(time_ur3-1.5,angle4_ur3*rtd+2, label='Rigid UR3 Robot')
plt.plot(time_sia5-1.7,angle4_sia5*rtd+5, label='Rigid SIA5 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 4 [deg]')
plt.xlim(0,5)
#plt.title('Torque')

plt.subplot(6,2,9)
plt.plot(time,-angle5_hebi*rtd+10, label='Series Elastic Robot')
plt.plot(time_ur3-1.5,-angle5_ur3*rtd-8, label='Rigid UR3 Robot')
plt.plot(time_sia5-1.7,-angle5_sia5*rtd+15, label='Rigid SIA5 Robot')
plt.legend()
#plt.xlabel('time [s]')
plt.ylabel('Angle 5 [deg]')
plt.xlim(0,5)


plt.subplot(6,2,11)
plt.plot(time,angle6_hebi*rtd+17, label='Series Elastic Robot')
plt.plot(time_ur3-1.5,angle6_ur3*rtd+3, label='Rigid UR3 Robot')
plt.plot(time_sia5-1.7,angle5_sia5*rtd-17, label='Rigid SIA5 Robot')
plt.legend()
plt.xlabel('time [s]')
plt.ylabel('Angle 6 [deg]')
plt.xlim(0,5)

plt.show()


