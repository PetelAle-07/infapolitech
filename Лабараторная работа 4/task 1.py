# TODO решите задачу
import json
def task() -> float:
    whole=0 # задаем значение для суммы произведений
    with open("input.json") as file:
        data = json.load(file)  # Десериализируем данные из JSON
        for set in data: # Проходим по занчениям в словаре
            whole+=(set.get("score")*set.get("weight")) # Прибавляем полученное произведение значений в заданную переменную
    return round(whole,4) # возвращаем полученное значение, округлив до 4


print(task())
