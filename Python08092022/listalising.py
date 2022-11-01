l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = l1
print(id(l1))
print(id(l2))
l1[5] = 200
print(l1)
print(l2)
