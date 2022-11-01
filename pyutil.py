import os
import psutil
load1 = psutil.getloadavg()
cpu_usage = (load1/os.cpu_count()) * 100

print("The CPU Usage is: ", cpu_usage)
