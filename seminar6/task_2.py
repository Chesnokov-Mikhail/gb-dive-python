# 2. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

from sys import argv
from date_time import checks_date_exist

if __name__ == "__main__":
    # Получаем дату на проверку в первом параметре
    date_str = argv[1:][0]
    if not date_str:
        date_str = input("Введите дату в формате DD.MM.YYYY: ")
    print(f"Дата {date_str} существует") if checks_date_exist(date_str) else print(f"Дата {date_str} НЕ существует")