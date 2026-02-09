import matplotlib.pyplot as plt

# Prepare x and y for plotting
x = [2018, 2019, 2020, 2021, 2022]
y = [10, 12, 15, 18, 22]

# Create the plot
plt.plot(x, y)

# Adding labels
# Add x axis label
plt.xlabel("Year")
# Add y axis label
plt.ylabel("Population in Million")

plt.show()