print("Welcome to my computr quiz!")

playing = input("Do you want to play ?")

if playing != "yes":
    quit()
print("Okay ! Let's Play: ")
answer = input("What does CPU stad for ?")
if answer == "central processing unit":
    print("Correct !")
else:
    print("Incorrect !")
answer = input("What does GPU stad for ?")
if answer == "graphical processing unit":
    print("Correct !")
else:
    print("Incorrect !")
answer = input("What does RAM stad for ?")
if answer == "random access memory":
    print("Correct !")
else:
    print("Incorrect !")
