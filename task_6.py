list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию

max_i = 0

for i,num in enumerate(list_numbers):
    if(num>= list_numbers[max_i]):
        max_i = i

temp = list_numbers[max_i]
list_numbers[max_i] = list_numbers[-1]
list_numbers[-1] = temp

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
