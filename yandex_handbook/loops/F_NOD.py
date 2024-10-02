a = int(input())
b = int(input())

while a != 0 and b != 0:
    if b > a:
        b = b % a
    elif a > b:
        a = a % b

print(a + b)
