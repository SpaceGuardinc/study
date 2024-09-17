
number = int(input())

number_1 = int(number % 10)
number_2 = int(number / 10 % 10)
number_3 = int(number / 100 % 10)

first = number_2 + number_3
second = number_2 + number_1

if second < first:
    print(f"{first}" + f"{second}")
else:
    print(f"{second}" + f"{first}")

