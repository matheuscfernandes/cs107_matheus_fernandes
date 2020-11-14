import numpy as np
import matplotlib.pyplot as plt
import datetime

def clock_hand(r):
    def hand_location(theta):
        theta = np.pi * theta / 180.0 # Convert to radians
        x = r * np.cos(theta) # x coordinate
        y = r * np.sin(theta) # y coordinate
        return x, y
    return hand_location

# Create some "instances" of clock hands
hour_hand = clock_hand(0.5)
minute_hand = clock_hand(0.75)
second_hand = clock_hand(1.0)

# Get the current time info
currentDT = datetime.datetime.now()

hour = currentDT.hour # Get hour
if (hour > 12):
    hour = hour - 12 # convert to twelve-hour clock

minute = currentDT.minute # Get minute
second = currentDT.second # Get seconds

print("{0}:{1}:{2}".format(hour, minute, second))

# Let's put these times on the clock. Convert to degrees.
theta_h = 90.0 - 30.0 * hour - 0.5 * minute
theta_m = 90.0 - 6.0 * minute
theta_s = 90.0 - 6.0 * second

# Now get some hand locations
x_hour, y_hour = hour_hand(theta_h)
x_minute, y_minute = minute_hand(theta_m)
x_second, y_second = second_hand(theta_s)

# And plot them to visualize

fig, ax = plt.subplots(1,1, figsize=(5,5))

ax.plot([0.0, x_hour], [0.0, y_hour], lw=4)
ax.plot([0.0, x_minute], [0.0, y_minute], lw=3)
ax.plot([0.0, x_second], [0.0, y_second], lw=1)

mini = -1.0
maxi = 1.0
ax.set_xlim(mini, maxi)
ax.set_ylim(mini, maxi)

ax.axis('off')

fig.savefig('clock.png', dpi=600)

plt.show()
