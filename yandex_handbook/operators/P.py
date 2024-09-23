petya = int(input())
vasya = int(input())
tolya = int(input())


first = max(petya, vasya, tolya)
third = min(petya, vasya, tolya)
second = petya + vasya + tolya - first - third

if first == petya:
    first_name = 'Петя'
elif first == vasya:
    first_name = 'Вася'
else:
    first_name = 'Толя'

if second == petya:
    second_name = 'Петя'
elif second == vasya:
    second_name = 'Вася'
else:
    second_name = 'Толя'

if third == petya:
    third_name = 'Петя'
elif third == vasya:
    third_name = 'Вася'
else:
    third_name = 'Толя'


print(f'{first_name: ^24}')
print(f'{second_name: ^8}{" ": ^16}')
print(f'{" ": ^16}{third_name: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')