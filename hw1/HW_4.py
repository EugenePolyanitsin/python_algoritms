# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ.

from random import randint, uniform, choice

print(randint(10, 20))
print(uniform(0.5, 1.5))
print(choice([chr(i) for i in range(ord('e'), ord('z'))]))
