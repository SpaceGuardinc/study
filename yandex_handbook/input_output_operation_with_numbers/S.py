product, price, weight, money = input(), int(input()), int(input()), int(input())
cost = f'{weight}кг * {price}руб/кг'
print(f'{'Чек':=^35}')
print(f'Товар:{product:>29}')
print(f'Цена:{cost:>30}')
print(f'Итого:{weight * price:>26}руб')
print(f'Внесено:{money:>24}руб')
print(f'Сдача:{money - weight * price:>26}руб')
print('=' * 35)