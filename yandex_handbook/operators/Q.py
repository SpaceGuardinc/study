a = float(input())
b = float(input())
c = float(input())

if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print(f"{x:.2f}")
else:
    desc = b ** 2 - 4 * a * c

    if desc > 0:
        x_1 = (-b - (desc ** 0.5)) / (2 * a)
        x_2 = (-b + (desc ** 0.5)) / (2 * a)
        if x_1 > x_2:
            x_1, x_2 = x_2, x_1
        print(f"{x_1:.2f} {x_2:.2f}")
    elif desc == 0:
        x = -b / (2 * a)
        print(f"{x:.2f}")
    else:
        print("No solution")

