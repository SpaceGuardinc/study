res = 0

while (b := float(input())) != 0:
    if b >= 500:
        res += b - (b / 100 * 10)
    else:
        res += b
print(res)