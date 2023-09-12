#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и
# знаменателем. Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

import fractions
import math

str_fraction_1 = input("Введите первую дробь в виде строки 'a/b': ")
str_fraction_2 = input("Введите вторую дробь в виде строки 'a/b': ")

# Разделяем на числитель и знаменатель
numerator_1, denominator_1 = str_fraction_1.split('/')
numerator_2, denominator_2 = str_fraction_2.split('/')

# Переводим в число
numerator_1_int = int(numerator_1)
denominator_1_int = int(denominator_1)
numerator_2_int = int(numerator_2)
denominator_2_int = int(denominator_2)

# Сложение дробей 1 и 2
# Находим наименьший общий множитель
denominator_summ = math.lcm(denominator_1_int, denominator_2_int)
# Вычисляем числитель суммы дробей
numerator_summ =  denominator_summ//denominator_1_int * numerator_1_int + \
                    denominator_summ//denominator_2_int * numerator_2_int

print(f"Сумма дробей {str_fraction_1} и {str_fraction_2} равна: {numerator_summ}/{denominator_summ}")
fraction_summ = fractions.Fraction(numerator_1_int, denominator_1_int) + fractions.Fraction(numerator_2_int, denominator_2_int)
print(f"Проверка суммы дробей через fractions: {fraction_summ}")

print("--"*30)

# Произведение дробей 1 и 2
numerator_multiplication =  numerator_1_int * numerator_2_int
denominator_multiplication = denominator_1_int * denominator_2_int

print(f"Умножение дробей {str_fraction_1} и {str_fraction_2} равна: {numerator_multiplication}/{denominator_multiplication}")

fraction_multiplication = fractions.Fraction(numerator_1_int, denominator_1_int) * fractions.Fraction(numerator_2_int, denominator_2_int)
print(f"Проверка умножения дробей через fractions: {fraction_multiplication}")
