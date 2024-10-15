i = int(input())

maximum = 0

while i > 0:
    digital = i % 10
    if digital > maximum:
        maximum = digital
    i = i // 10


print(maximum)
