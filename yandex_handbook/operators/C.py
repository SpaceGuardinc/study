
a = int(input())
b = int(input())
c = int(input())
if (a > b) & (a > c):
    print("Петя")
elif (b > c) & (b > a):
    print("Вася")
else:
    print("Толя")