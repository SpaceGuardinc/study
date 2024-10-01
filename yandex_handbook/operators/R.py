a = int(input())
b = int(input())
c = int(input())


if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
    print("100%")
elif a ** 2 < b ** 2 + c ** 2 and b ** 2 < a ** 2 + c ** 2 and c ** 2 < a ** 2 + b ** 2:
    print("крайне мала")
else:
    print("велика")