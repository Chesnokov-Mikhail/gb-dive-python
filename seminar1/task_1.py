# 1.Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
width_column = 10
width_spase = 5
width_table = width_spase * 3 + width_column * 4
print(f"{'ТАБЛИЦА УМНОЖЕНИЯ':^{width_table}}")
# минимальное значение 1-го множителя
min_multiplier1 = 2
# максимальное значение 1-го множителя
max_multiplier1 = 9
# минимальное значение 2-го множителя
min_multiplier2 = 2
# максимальное значение 2-го множителя
max_multiplier2 = 10
# количество строк таблицы
count_row = 2

for k in range(0,count_row):
    for i in range(min_multiplier2,max_multiplier2 + 1):
        for j in range(min_multiplier1 + (max_multiplier1 // count_row) * k, \
                       max_multiplier1 // count_row + (max_multiplier1 // count_row) * k + 2):
            print(f"{j} X {i:<2}={i * j:>3}", end=" " * width_spase)
        print()
    print()