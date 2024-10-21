# TODO Найдите количество книг, которое можно разместить на дискете
available_space_Mb = 1.44 #Обьем дискеты в Мб
available_space_Kb = 1.44*1024
available_space_b = available_space_Kb*1024

symb_space = 4 #utf-32, не ты ли это?
symb_in_page = 25
strings_on_page = 50
pages_in_book = 100

size_of_book = symb_space * symb_in_page * strings_on_page * pages_in_book

max_books_in_disk = int(available_space_b // size_of_book)


print("Количество книг, помещающихся на дискету:", max_books_in_disk)
