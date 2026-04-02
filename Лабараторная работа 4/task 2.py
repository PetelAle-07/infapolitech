# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data=[]
    with open(INPUT_FILENAME, "r") as file:
        reader = csv.DictReader(file) # десерелизируем данные из CSV файла
    # TODO считать содержимое csv файла
        for row in reader:
            data.append(row) # Считатываем содержимое csv файла
    # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False) # Сериализируем в JSON, с отступом в 4
    return data # Входит json строка


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
