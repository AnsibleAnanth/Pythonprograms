print("--------To find Prime Number--------")
num = int(input("Enter the Number"))
count = 0
for i in range(1, num+1):
    if num % i == 0:
        count += 1
if count == 2:
    print("Prime Number")

else:
    print("Not a Prime Number..")
