# минимальное и максимальное значение координат на шахмотной доске
MIN_COORDINAT = 1
MAX_COORDINAT = 8

def check_beat_queen(coordinats: list()) -> bool:
    """
    Определяет имеется ли пара бьющих друг друга ферзей по списку координат ферзей на шахматной доске
    :param coordinats: список координат [(int, int)], где (координата по горизонтали, координата по вертикали)
    :return: True если нет бьющих друг друга ферзей, в противном случае False
    """
    coordinats_h_set = {item[0] for item in coordinats}
    coordinats_v_set = {item[1] for item in coordinats}
    # Если есть повторяющиеся координаты по горизонтали или вертикали , то есть пара бьющих друг друга ферзей
    if len(coordinats_h_set) < len(coordinats) or len(coordinats_v_set) < len(coordinats):
        return False
    while coordinats:
        queen = coordinats.pop()
        # проход по диагонали влево и вниз
        for (h,v) in ((queen[0] - i, queen[1] - i) for i in range(1,MAX_COORDINAT)
                      if ((queen[0] - i) >= MIN_COORDINAT or (queen[1] - i) >= MIN_COORDINAT)):
            if (h,v) in coordinats:
                return False
        # проход по диагонали влево и вверх
        for (h,v) in ((queen[0] - i, queen[1] + i) for i in range(1,MAX_COORDINAT)
                      if ((queen[0] - i) >= MIN_COORDINAT or (queen[1] + i) <= MAX_COORDINAT)):
            if (h,v) in coordinats:
                return False
        # проход по диагонали вправо и вниз
        for (h,v) in ((queen[0] + i, queen[1] - i) for i in range(1,MAX_COORDINAT)
                      if ((queen[0] + i) <= MAX_COORDINAT or (queen[1] - i) >= MIN_COORDINAT)):
            if (h,v) in coordinats:
                return False
        # проход по диагонали вправо и вверх
        for (h,v) in ((queen[0] + i, queen[1] + i) for i in range(1,MAX_COORDINAT)
                      if ((queen[0] + i) <= MAX_COORDINAT or (queen[1] + i) <= MAX_COORDINAT)):
            if (h,v) in coordinats:
                return False
    return True