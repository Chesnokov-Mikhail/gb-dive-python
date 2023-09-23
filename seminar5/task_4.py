# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def gen_fibonachi_number(number: int) -> int:
    """
    Генератор последовательности Фибоначи
    :param number: порядковый номер элемента числа Фибоначи
    :return: объект генератор
    """
    # fib_ = [0,1]
    # for i in range(0, number):
    #     if i == 0:
    #         fib_num = 0
    #     elif i == 1:
    #         fib_num = 1
    #     else:
    #         fib_num = sum(fib_)
    #         fib_[0],fib_[1] = fib_[1], fib_num
    first, second = 0, 1
    for i in range(0, number):
        yield first
        first, second = second, first+second

def main():
    num = int(input("Введите номер элемента ряда Фибоначи: "))
    print(f"Последовательность ряда Фибоначи до {num} элемента: ", *gen_fibonachi_number(num))

if __name__ == "__main__":
    main()