name = str(input())
number = int(input())

first_symbol = int(number / 100)
second_symbol = int(number % 10)
third_symbol = int(number / 10 % 10)

print("Группа " + f"№{first_symbol}.")
print(f"{second_symbol}. " + f"{name}.")
print("Шкафчик:", f"{number}.")
print("Кроватка:", f"{third_symbol}.")
