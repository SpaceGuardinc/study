from sympy import prime

a = float(input())
b = float(input())
c = float(input())



#a * x ** 2 + b * x + c

desc = b ** 2 - 4 * a * c

if desc > 0:
    x_1 = (-b + desc ** 0.5) / 2 * a
    x_2 = (-b - desc ** 0.5) / 2 * a
    print(f"{x_1:.2f}, {x_2:.2f}")
elif desc < 0:
    print("No solution")
elif a == 0.0 and b == 0.0 and c == 0.0:
    print("Infinite solutions")
elif desc == 0:
    x = -b / (2 * a)
    print(f"{x:.2f}")
