import psutil
import GPUtil

print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)

GPUtil.showUtilization()
