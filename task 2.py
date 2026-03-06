symb_bite=4 # Размер одного символа
symb_num=25 # Количество символов в строке
num_lines=50 # Число строк на странице
pages=100 # Количество страниц
disk_size=1.44 # Размер диска
weight_book_bite=(symb_bite*symb_num*num_lines*pages) # Считаем размер книги в байтах
book_in_mb=weight_book_bite/1024/1024 # Переводим размер книги в мегабайты
amount_of_books=disk_size//book_in_mb # Считаем количество книг помещающихся на диске

print("Количество книг, помещающихся на дискету:", int(amount_of_books)) # Выводим переведя в integer

