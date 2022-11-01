def add(a, b):
    b = b+a
    if a == 1:
        print(b)
    elif a > 1:
        add(a-1, b)


add(range, 0)
