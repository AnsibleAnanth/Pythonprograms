print("Enter the limit to find Prime Numbers:")
s = int(input())
e = int(input())
for n in range(s, e + 1):
    if(n > 1):
        for i in range(2, n):
            if (n % i) == 0:
                break
        else:
            print(n)
