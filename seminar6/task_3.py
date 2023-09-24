# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint as rndi
from chess_board import check_beat_queen
from chess_board import MIN_COORDINAT
from chess_board import MAX_COORDINAT
from chess_board import queen_random_placement

# количество ферзей
COUNT_QUEEN = 8

if __name__ == "__main__":
    # генерируем уникальные пары координат для случайной расстановки COUNT_QUEEN ферзей
    queen_place = queen_random_placement(COUNT_QUEEN, MIN_COORDINAT, MAX_COORDINAT)
    # определяем, есть ли среди ферзей пара бьющих друг друга
    result = check_beat_queen(queen_place)
    print(f"Координаты ферзей: {queen_place}", "Ферзи НЕ бьют друг друга" if result else "Ферзи бьют друг друга", sep="\n")