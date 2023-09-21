# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

def gen_simple_number(stop_number: int) -> int:
    """
    Генератор простых чисел
    :param stop_number: граница нахождения простых чисел
    :return: объект генератор
    """
    for i in range(2, stop_number+1):
        # true - простое число, false - составное число
        simple = True
        # не проверяем первый простые числа 2 и 3
        if not (i == 2 or i == 3):
            # не выводим четные числа
            if not i % 2:
                continue
            # Проверка на простое число
            for j in range(3, int(i**0.5)+1, 2):
                if not i % j:
                    simple = False
                    break
            if not simple:
                continue
        yield i

def main():
    num = int(input("Введите границу вывода простых чисел: "))
    print(f"Последовательность простых чисел до {num}: ", *gen_simple_number(num))

if __name__ == "__main__":
    main()