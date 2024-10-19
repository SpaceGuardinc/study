count_roads = int(input())
counter = 0

for i in range(count_roads):
    roads = input()
    if 'зайка' in roads:
        counter += 1

print(counter)
