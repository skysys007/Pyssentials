import matplotlib
import matplotlib.pyplot as plt
# the pyplot module contains the core plotting functionality of matplotlib
# the plt is used as an alias
print(matplotlib.__version__)

# Creating a simple figure object
# A figure is a top level container for all the plot elements, or sort of a canvas
# Axes(subplots) is the area where the data is plotted
# subplots() - returns a tuple containing a figure and an axes object 

# Creating figure and axes
fig, ax = plt.subplots()
#savefig saves the figure to a file
plt.savefig("empty_plot.png")