
a = int(input())
b = int(input())
c = int(input())
if ((a > b) & (a > c)) & (b > c):
    print("1. Петя")
    print("2. Вася")
    print("3. Толя")
elif ((a > b) & (a > c)) & (c > b):
    print("1. Петя")
    print("2. Толя")
    print("3. Вася")
elif ((b > c) & (b > a)) & (a > c):
    print("1. Вася")
    print("2. Петя")
    print("3. Толя")
elif ((b > c) & (b > a)) & (c > a):
    print("1. Вася")
    print("2. Толя")
    print("3. Петя")
elif ((c > a) & (c > b)) & (b > a):
    print("1. Толя")
    print("2. Вася")
    print("3. Петя")
elif ((c > a) & (c > b)) & (a > b):
    print("1. Толя")
    print("2. Петя")
    print("3. Вася")