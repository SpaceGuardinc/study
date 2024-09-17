number: int = int(input())

number_3 = int(number / 100 % 10)
number_2 = int(number / 10 % 10)
number_1 = int(number % 10)


min_number = (min(number_1, number_2, number_3))
max_number = (max(number_1, number_2, number_3))

average = number_1 + number_2 + number_3 - max(number_1, number_2, number_3) - min(number_1, number_2, number_3)

if min_number + max_number != average * 2:
    print("NO")
else:
    print("YES")
