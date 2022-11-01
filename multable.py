
def time_table():
    x = int(input("Enter the Value: "))
    for row in range(x):
        for col in range(x):
            print(row*col, end=" ")
            print()


time_table()
