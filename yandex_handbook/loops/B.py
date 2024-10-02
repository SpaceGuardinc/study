counter = 0

while (stop := input()) != "Приехали!":
    if 'зайка' in stop:
        counter += 1
print(counter)
