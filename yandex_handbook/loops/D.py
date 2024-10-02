start = int(input())
finish = int(input())

if start > finish:
    for i in range(start, finish - 1, -1):
        print(i, end=' ')
else:
    for i in range(start, finish + 1):
        print(i, end=" ")

