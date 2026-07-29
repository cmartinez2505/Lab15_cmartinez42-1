"""
Program Name: Sine Wave Plotter
Author: Chris Martinez
Purpose: Plots a sine wave using matplotlib
Starter Code: None
Date: July 28, 2026
"""

#My libaries used for the lab
import math
import matplotlib.pyplot as plt


#Created my empty lists for coordinates
x = []
y = []


#Loop through 0 to 360, convert to radians, then calculate sine
for degree in range(361):
    radian = math.radians(degree)
    x.append(radian)
    y.append(math.sin(radian))

#Data plotted
plt.plot(x, y)

#Added title and labels
plt.title("Sine Wave")
plt.xlabel("X Axis (Radians)")
plt.ylabel("Y Axis")