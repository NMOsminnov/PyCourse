list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

# TODO найти сумму, количество и среднее арифметическое уникальных чисел
uniq = set(list_)

uniq_sum = sum(uniq)
uniq_len = len(uniq)
uniq_avg = round(uniq_sum/uniq_len,5)

dict_ = {
"Сумма уникальных чисел:"                   : uniq_sum,
"Количество уникальных чисел:"              : uniq_len,
"Среднее арифметическое уникальных чисел:"  : uniq_avg
}

print(dict_)
