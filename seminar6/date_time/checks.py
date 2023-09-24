from calendar import isleap

# минимальный и максимальный допустимый год
MINYEAR = 1
MAXYEAR = 9999

def _leap_year(year: int) -> bool:
    """
    Проверка года на високосность
    :param year: проверяемый год в формате YYYY
    :return: True если год високосный, иначе False
    """
    return isleap(year)
def checks_date_exist(date_check: str) -> bool:
    """
    Проверка корректности введенной даты в диапазоне от 01.01.0001 до 31.12.9999
    :param date_check: дата в формате "DD.MM.YYYY"
    :return: True если дата корректна, иначе False
    """
    month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    day, month, year = list(map(int,date_check.split(".")))
    # проверка года на вхождение в допустимый диапазон
    if not (MINYEAR <= year <= MAXYEAR):
        return False
    # Проверка года на високостность
    if _leap_year(year):
        month_dict[2] = 29
    else:
        month_dict[2] = 28
    # проверка месяца и дня на допустимость значения
    if not (0 < day <= month_dict.get(month, -1)):
        return False
    return True

if __name__ == "__main__":
    print(checks_date_exist("29.02.2023"))
    print(checks_date_exist("29.02.2020"))
    print(checks_date_exist("31.06.2023"))
    print(checks_date_exist("-1.02.2023"))