sum_ = 0  # заводим переменную счетчик, в которой мы будем считать сумму
n = 1  # текущее натуральное число
max_sum = 250

# заводим цикл while, который будет работать пока сумма не превысит 250
# TODO переписать на цикл с постусловием
while True:
    sum_ += n  # увеличиваем сумму, равносильно sum_ = sum_ + n

    n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную счетчик
    print("Ещё считаю ...", sum_)
    if sum_ > max_sum: #условие выхода
        break



print("Количество чисел: ", n)

