# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

m = []

for i in range(4):
    m.append([])
    sum = 0
    for n in range(4):
        user_number = int(input(f'Введите элемент {i+1} и {n+1} столбца: '))
        sum += user_number
        m[i].append(user_number)

    m[i].append(sum)

for a in m:
    print(('{:>4d}' * 5).format(*a))
