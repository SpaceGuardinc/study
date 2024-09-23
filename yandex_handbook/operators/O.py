a = int(input())
b = int(input())

a_1 = int(a % 10)
a_2 = int(a / 10 % 10)

b_1 = int(b % 10)
b_2 = int(b / 10 % 10)

maximum = max(a_1, b_1, a_2, b_2)
minimum = min(a_1, b_1, a_2, b_2)

res = a_1 + b_1 + a_2 + b_2 - maximum - minimum


if res >= 10:
    res = int(res % 10)

print(f"{maximum}" + f"{res}" + f"{minimum}")
