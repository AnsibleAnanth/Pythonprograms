# s = int(input("Enter the Number:"))
# i = 0
# while (i < s):
#     print(i)
#     i = i+1
sno = int(input("Enter the Secret Number"))
gcount = 0
glimit = 3

while gcount < glimit:
    guess = int(input("Guess:"))
    gcount += 1
    if guess == sno:
        print("You Won..")
        break
