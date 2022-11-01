import pygal
file = open('D:\VSCode Python\Python Exercise\pets.txt', 'r')
data = file.read().splitlines()
barchart = pygal.Bar()
for i in data:
    broken = i.split(' ')
    barchart.add(broken[0], int(broken[1]))
barchart.render()
