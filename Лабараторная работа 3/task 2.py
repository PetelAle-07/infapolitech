# TODO Напишите функцию find_common_participants
def find_common_participants(first_string, second_string, spliter_=","):
    first_string_set = set(first_string.split(spliter_)) # создаем множество первой строки
    second_string = set(second_string.split(spliter_)) # создаем множество второй строки
    comon = list(first_string_set & second_string) # ищем общие имена среди двух множеств
    return comon


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, spliter_="|")) # вызываем функцию заменив аргумент по умолчанию

