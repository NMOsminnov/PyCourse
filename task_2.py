a = 73
b = 10
c = 55

condition_1 = a<45 and b>=45 and c>=45  # TODO записать условие, что только первое число меньше 45
condition_2 = b<45 and a>=45 and c>=45 # TODO записать условие, что только второе число меньше 45
condition_3 = c<45 and b>=45 and a>=45 # TODO записать условие, что только третье число меньше 45

if condition_1 or condition_2 or condition_3:  # TODO объединить три условия с помощью нужного логического оператора and или or
    print("Одно из чисел меньше 45")
