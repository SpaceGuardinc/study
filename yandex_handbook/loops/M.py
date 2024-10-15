# Вывод слова с минимальным кол-во символов
count_players = int(input())

minimum_name = None

for i in range(count_players):
    name_players = input()
    if minimum_name is None:
        minimum_name = name_players
    elif len(name_players) < len(minimum_name):
        minimum_name = name_players

print(minimum_name)

# Вывод слова которое лексигнафически минимальное

# count_players = int(input())
#
# minimum_name = None
#
# for i in range(count_players):
#     name_players = input()
#     if minimum_name is None:
#         minimum_name = name_players
#     elif name_players < minimum_name:
#         minimum_name = name_players
#
# print(minimum_name)