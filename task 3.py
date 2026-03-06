players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle = len(players) // 2 # Высчитываем середину списка
first_team = players[:middle] # Выделяем игроков для первой команды
second_team = players[middle:] #Выделяем игроков для второй команды
print(first_team)
print(second_team)
