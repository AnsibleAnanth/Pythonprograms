import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('D:\VSCode Python\Python Exercise\price.csv')

x = df['Model']
y = df['Price']
# Bar Chart
# plt.xlabel('Model', fontsize=18)
# plt.ylabel('Price Rs', fontsize=16)
# plt.bar(x, y)
# Pie Chart
# plt.pie(y, labels=x, radius=1.2, autopct='%0.01f%%',
#         shadow=True, explode=[.05, .2, .05, .2, .05, .2, .05])
# Line Graph
plt.xlabel('Model', fontsize=18)
plt.ylabel('Price($)', fontsize=16)
plt.scatter(x, y)
plt.plot(x, y)

plt.show()
