from dataclasses import dataclass
import pandas as pd
import csv
import openpyxl
# df = pd.read_csv('D:\VSCode Python\Python Script\cpu.txt',
#                  sep='\s+', header=None)
# df.to_excel('cpu.xlsx', 'sheet1')
input_file = r"D:\VSCode Python\Python Script\mpstat.txt"
output_file = "mpstat.xlsx"

wb = openpyxl.Workbook()
ws = wb.worksheets[0]

with open(input_file, 'r') as data:
    reader = csv.reader(data, delimiter='\t')
    for row in reader:
        ws.append(row)
wb.save(output_file)
