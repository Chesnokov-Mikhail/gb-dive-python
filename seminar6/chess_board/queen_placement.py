from random import randint as rndi
from random import shuffle
from itertools import combinations

def queen_random_placement(count: int, min_coordinat: int, max_coordinat: int) -> list:
    """
    генерирует уникальные пары координат для случайной расстановки count ферзей
    :param count: количество ферзей
    :param min_coordinat: минимальная координата размещения
    :param max_coordinat: максимальная координата размещения
    :return: список координат ферзей [(int, int)], где (координата по горизонтали, координата по вертикали)
    """
    coordinats_set = set()
    while len(coordinats_set) < count:
        coordinats_set.add((rndi(min_coordinat, max_coordinat), rndi(min_coordinat, max_coordinat)))
    return list(coordinats_set)

def queen_full_placement(count: int, min_coordinat: int, max_coordinat: int) -> combinations:
    """
    Возвращает сочетания (уникальные пары координат) возможной расстановки count ферзей на поле размером min_coordinat на max_coordinat
    :param count: количество размещаемых ферзей
    :param min_coordinat: минимальная координата размещения
    :param max_coordinat: максимальная координата размещения
    :return: combinations из itertools
    """
    full_list_coordinats = [(h, v) for h in range(min_coordinat, max_coordinat + 1) for v in range(min_coordinat, max_coordinat + 1)]
    shuffle(full_list_coordinats)
    return combinations(full_list_coordinats, count)