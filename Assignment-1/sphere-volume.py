#%% Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r 3
import math
diameter = 12
volume = (4/3) * math.pi * (diameter/2) ** 3
print(volume)