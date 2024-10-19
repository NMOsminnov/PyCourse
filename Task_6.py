results = [10, 8, 9, 7, 6, 9, 10, 8, 9, 10]

# TODO Вычислите необходимые значения
total = sum(results)
count = len(results)
avg = total/count
min = min(results)
max = max(results)

print("Среднее арифметическое результатов выстрелов:", avg)
print("Наименьшее количество очков за выстрел:", min)
print("Наибольшее количество очков за выстрел:", max)
