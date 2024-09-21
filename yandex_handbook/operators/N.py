a = int(input())

number_1 = int(a % 10)
number_2 = int(a / 10 % 10)
number_3 = int(a / 100 % 10)


min_number = (min(str(number_3) + str(number_2),
                  str(number_3) + str(number_1),
                  str(number_1) + str(number_2),
                  str(number_1) + str(number_3),
                  str(number_2) + str(number_3),
                  str(number_2) + str(number_1)))

max_number = (max(str(number_3) + str(number_2),
                  str(number_3) + str(number_1),
                  str(number_1) + str(number_2),
                  str(number_1) + str(number_3),
                  str(number_2) + str(number_3),
                  str(number_2) + str(number_1)))


if int(min_number) < 10:
    min_number = int(min_number) * 10
    if int(min_number) < 10:
        min_number = int(min_number) + number_2

if int(min_number) < 10:
    min_number = int(min_number) * 10
    if int(min_number) < 10:
        min_number = int(min_number) + number_3

print(min_number, max_number)
