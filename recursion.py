def countdown(i: int):
    print(i)
    if i-1 >= 0:
        countdown(i-1)

countdown(10)
