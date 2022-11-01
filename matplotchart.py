import time
from tkinter.ttk import Notebook
import psutil
import matplotlib.pyplot as plt

plt.rcParams['animation.html'] = 'jshtml'
fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

i = 0
x, y = [], []
while True:
    x.append(i)
    y.append(psutil.cpu_percent())
    ax.plot(x, y, color='b')
    fig.canvas.draw()

    time.sleep(1)
    i = i+1
