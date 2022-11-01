import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('pets.txt', 'r')
size = np.shape(data)
print("Size of Data Set= ", size)

time = data[:, 0]
mode = data[:, 1]

plt.figure()
plt.plot(time, mode)
plt.xlabel('Time(Sec)')
plt.ylabel('Mode')
plt.grid()
