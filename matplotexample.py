import matplotlib.pyplot as pt
from matplotlib.animation import FuncAnimation
from psutil import cpu_percent

usage = cpu_percent()
print(usage)
