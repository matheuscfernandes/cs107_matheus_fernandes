import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import datetime

### Closure defined up here
def Clock(r):
    def Time(theta):
        rad_theta=np.deg2rad(theta)
        x=r*np.cos(rad_theta)
        y=r*np.sin(rad_theta)
        return x,y
    
    return Time

currentDT = datetime.datetime.now()
hour = currentDT.hour
minute = currentDT.minute
second = currentDT.second

# Calculate theta in degrees for each hand

theta_hour=90.-30.*hour-minute/2.
theta_min=90.-6*minute
theta_sec=90-6*second

# Specify the length of hour, minute and second hands
length_of_hour_hand=0.8
length_of_min_hand=1
length_of_sec_hand=1.2

# hour_hand = name_ofss_closure(length_of_hour_hand)
hour_hand=Clock(length_of_hour_hand)
min_hand=Clock(length_of_min_hand)
sec_hand=Clock(length_of_sec_hand)

x_hour, y_hour = hour_hand(theta_hour)
x_min, y_min = min_hand(theta_min)
x_sec, y_sec = sec_hand(theta_sec)

# Plot the clock
figure, axes = plt.subplots()

#Creating the clock numbers
plt.text(sec_hand(0)[0],sec_hand(0)[1],'3',fontsize=20,horizontalalignment='center',verticalalignment='center')
plt.text(sec_hand(90)[0],sec_hand(90)[1],'12',fontsize=20,horizontalalignment='center',verticalalignment='center')
plt.text(sec_hand(-90)[0],sec_hand(-90)[1],'6',fontsize=20,horizontalalignment='center',verticalalignment='center')
plt.text(sec_hand(180)[0],sec_hand(180)[1],'9',fontsize=20,horizontalalignment='center',verticalalignment='center')

#plotting the different arms of the clock
thickness=5
colors=['g','b','r']
plt.plot([0,x_hour],[0,y_hour],lw=thickness,c=colors[0])
plt.plot([0,x_min],[0,y_min],lw=thickness*0.7,c=colors[1])
plt.plot([0,x_sec],[0,y_sec],lw=thickness*0.4,c=colors[2])

plt.xlim([-1.4,1.4])
plt.ylim([-1.4,1.4])

#creating clock circle
circ=plt.Circle((0,0),1.4,color='gray')
axes.add_artist(circ)
axes.set_aspect('equal','box')


plt.show()