# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

x1, y1 = int(input('Enter coordinates x1')), int(input('Enter coordinates y1'))
x2, y2 = int(input('Enter coordinates x2')), int(input('Enter coordinates y2'))

k = (y1 - y2) / (x1 - x2)
b = y1 - k * x1
sign = '+' if b > 0 else '-'
print(f'y = {k} * {sign} {abs(b)}')
