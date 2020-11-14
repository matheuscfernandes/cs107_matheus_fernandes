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
hour_hand = clock_hand(1.0)
minute_hand = clock_hand(0.75)
second_hand = clock_hand(0.5)

fig = plt.figure(figsize=(5,5))

s0 = 1.0
while True:
    plt.cla()

    # Get the current time info
    currentDT = datetime.datetime.now()
    
    hour = currentDT.hour # Get hour
    if (hour > 12):
        hour = hour - 12 # convert to twelve-hour clock
    
    minute = currentDT.minute # Get minute
    second = currentDT.second # Get seconds
    
    # Let's put these times on the clock. Convert to degrees.
    theta_h = 90.0 - 30.0 * hour - 0.5 * minute
    theta_m = 90.0 - 6.0 * minute
    theta_s = 90.0 - 6.0 * second

    # Now get some hand locations
    x_hour, y_hour = hour_hand(theta_h)
    x_minute, y_minute = minute_hand(theta_m)
    x_second, y_second = second_hand(theta_s)
    
    # And plot them to visualize
    plt.axis([-1.0, 1.0, -1.0, 1.0])
    
    plt.plot([0.0, x_hour], [0.0, y_hour], lw=4)
    plt.plot([0.0, x_minute], [0.0, y_minute], lw=4)
    plt.plot([0.0, x_second], [0.0, y_second], lw=4)

    fig.canvas.draw()
    plt.pause(0.1)

    if second == s0:
       break
