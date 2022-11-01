# Importing the numpy and visualization library
import numpy as np
import matplotlib.pyplot as plt
# Plotting the axis
plt.axis([0, 10, 0, 1])
# Creating a random scatter plot
for i in range(10):
    y = np.random.random()
    plt.scatter(i, y)
    plt.pause(0.05)
plt.show()
