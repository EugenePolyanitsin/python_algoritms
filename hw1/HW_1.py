# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = input('Enter your number: ')
b = 0
c = 0
for letter in a:
    b += int(letter)
    c *= int(letter)
print(b, c)
