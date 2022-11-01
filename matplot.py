import numpy as np
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
data = np.genfromtxt('D:\VSCode Python\mpstat.txt', delimiter=',')
print(data)
sum = 0
Content = ["Time", "CPU", "%usr", "%nice", "%sys", "%iowait",
           "%irq", "%soft", "%steal", "%guest", "%gnice", "%idle"]
l_sum = []
for i in data:
    print(i)
for i in range(len(data[0])):
    sum = 0
    for j in range(len(data)):
        sum = sum+data[i][j]
    l_sum.append(sum)
print(l_sum)
plt1.plot(data)
plt1.xlabel("Cpu Usage")
plt1.ylabel("Cpu Usage")
plt1.legend(Content)
plt2.plot(l_sum)
plt1.show()
plt2.show()
