import pandas as pd
data1 = pd.read_csv('mpstat.txt')
data1.to_csv('mpstat.csv', index=None)
