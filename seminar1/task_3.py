#3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input("Вводите целое положительное число меньше 100 тысяч: "))
if num < 0:
    print(f"Число {num} отрицательное. Введите положительное число.")
    exit()
elif num > 100000:
    print(f"Число {num} больше 100 тысяч. Введите меньшее число.")
    exit()
elif num == 0:
    print(f"Введите число больше 0.")
    exit()
# наименьший делитель
min_divisor = int(num**0.5)
# true - простое число, false - составное число
simple = True

for i in range(2,min_divisor+1):
    if num % i == 0:
        simple = False
        break

if simple:
    print(f"Число {num} является простым")
else:
    print(f"Число {num} является составным")