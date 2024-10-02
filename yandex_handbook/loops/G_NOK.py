a = int(input())
b = int(input())

z = a

x = b

while a != 0 and b != 0:
    if b > a:
        b = b % a
    elif a > b:
        a = a % b

noda = a + b

print(int(x * z / noda))

