a = int(input())
b = int(input())
c = int(input())


number_1 = int(a / 10 % 10)
number_2 = int(b / 10 % 10)
number_3 = int(c / 10 % 10)

number_6 = int(c % 10)
number_4 = int(a % 10)
number_5 = int(b % 10)

if number_1 == number_2 == number_3:
    print(number_1)
else:
    print(number_4)