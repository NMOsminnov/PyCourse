numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
missing_ind = numbers.index(None)

sum_without_missing = sum(num for num in numbers if num is not None)
average_value = sum_without_missing / (len(numbers)) #Разве тут не должно быть len-1?
#Или я чего-то не знаю про len?

numbers[missing_ind] = average_value



print("Измененный список:", numbers)
