
a = float(input())

while a != 0:
    if a >= 500:
        a = a - (a / 100 * 10)
    else:
        a = a + a

print(a)
