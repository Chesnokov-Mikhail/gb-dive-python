# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

from chess_board import check_beat_queen
from chess_board import MIN_COORDINAT
from chess_board import MAX_COORDINAT
from chess_board import queen_random_placement
from chess_board import queen_full_placement

# количество ферзей
COUNT_QUEEN = 8

if __name__ == "__main__":
    # уникальные пары координат для случайной расстановки COUNT_QUEEN ферзей
    queen_place = queen_random_placement(COUNT_QUEEN, MIN_COORDINAT, MAX_COORDINAT)
    print(f"Координаты для случайной расстановки {COUNT_QUEEN} ферзей: \n {queen_place} ")
    # Проверяем различные случайные варианты и выводим первые count успешные расстановки.
    count = 4
    print("Координаты ферзей, которые НЕ бьют друг друга:")
    for place in queen_full_placement(COUNT_QUEEN, MIN_COORDINAT,MAX_COORDINAT):
        if check_beat_queen(list(place)):
            print(place)
            count -= 1
        if count <= 0:
            break

