from math import factorial


num=int(input("Enter the limt for Factorial :"))
factorial =1
if num < 0:
    print("Enter the Positive Value :")
elif num == 0:
    print("factorial = 1")

else:
    for i in range (1,num + 1):
        factorial=factorial * i
print(factorial)    

