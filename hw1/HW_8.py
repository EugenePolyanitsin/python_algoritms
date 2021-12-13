# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Enter year: '))
if year % 400 + year % 4 == 0 * year % 100 != 0 == 0:
    print(True)
else:
    print(False)
