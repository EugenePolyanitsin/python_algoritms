# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
a, b, c = sorted([a, b, c])
print(f'min {a}, middle {b}, max {c}')
