print("##### PRIME NUMBER PROGRAM #####")
count = 0
number = int(input("Enter the Number to find: "))
for i in range(2, number+1):
    if number % i == 0:
        count += 1

if count == 2:
    print("Give Number is Prime :", number)
else:
    print("Given Number is Not Prime:", number)
