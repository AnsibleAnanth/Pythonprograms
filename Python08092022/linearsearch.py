a = [10, 20, 3, 0, 1]
no = 0
count = 0
for i in a:
    count += 1
    if i == no:
        print("True")
        print(a)
        break
    elif count == len(a):
        print("False")
        print(a)
