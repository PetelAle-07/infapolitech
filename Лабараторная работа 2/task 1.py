money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0 # счетчик месяцев
while money_capital + salary >= spend: # while т.к.неизвестно количество месяцев
    money_capital = money_capital + salary - spend # изменение фин. подушки
    month = month + 1 # изменение месяца
    spend=spend + (spend*increase) # изменение трат
print("Количество месяцев, которое можно протянуть без долгов:", month)
