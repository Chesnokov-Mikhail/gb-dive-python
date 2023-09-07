#4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
#from random import
#randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num_random = randint(LOWER_LIMIT, UPPER_LIMIT)
print("Угадайте число за 10 попыток.")
for i in range(0, 10):
    num = int(input("Введите число: "))
    if num > num_random:
        print("загаданное число меньше")
    elif num < num_random:
        print("загаданное число больше")
    else:
        print("угадали загаданное число")
        break