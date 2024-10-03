
x = 0
y = 0

while (word := str(input())) != "СТОП":
    number = int(input())
    if word == "СЕВЕР":
        y += number
    elif word == "ЮГ":
        y -= number
    elif word == "ЗАПАД":
        x -= number
    elif word == "ВОСТОК":
        x += number


print(y)
print(x)
