import random
n = 20
gussed = int (n * random.random()) + 1
guess = 0
while guess  != gussed :
        guess = int (input("Enter New Number :"))
        if guess > 0:
            if guess > gussed: 
              print("Number to Large :")
        elif guess < gussed:
             print("Number to Small")

        else:
             print("That you are giving up :")
             break
else:
      print("Congratulation you made it..")           
