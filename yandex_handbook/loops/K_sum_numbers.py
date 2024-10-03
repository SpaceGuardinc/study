# numbers = input()
#
# res = 0
#
# for i in range(len(numbers)):
#     x = int(numbers) % 10
#     numbers = int(numbers) / 10
#     res += x
#
# print(res)

num = int(input())

summa = 0

while num > 0:
    summa += num % 10  # s = s + num % 10
    num //= 10  # num = num // 10

print(summa)
