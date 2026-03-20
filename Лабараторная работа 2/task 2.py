salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = 0 # Изначальная подушка безопасности
for months in range(1, months + 1): # for т.к. известно количество месяцев
    if months > 1:
        spend = spend + (spend*increase) # после первого месяца траты увеличиваются
    if spend > salary:
        money_capital= money_capital + (spend - salary) # изменение фин. подушки
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
