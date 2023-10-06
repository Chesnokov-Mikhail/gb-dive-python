# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
from random import randint as rndi
from work_file import save_csv, load_csv, save_json
from typing import Callable

PATH_CSV = ".\Array.csv"
PATH_JSON = ".\out_resolve.json"

def generator_koeficient(number: int, min: int, max: int) -> list:
    """
    Генератор коэфицентов квадратного уравнения (a,b,c)
    :param number: количество наборов коэфицентов
    :param min: минимальное число для генерации коэфициента
    :param max: максимальное число для генерации коэфициента
    :return: список наборов коэфицентов [(int,int.int)]
    """
    return list([(rndi(min, max), rndi(min, max), rndi(min, max)) for i in range(number)])

def output_json(path_json: str):
    """
    Декоратор сохранения результатов в JSON
    :param path_json: путь к JSON
    :return: в случае успешного сохранения True, иначе False
    """
    def decor_save_json(func: Callable):
        def wrapper(*args):
            result = func(*args)
            res = save_json(result, path_json)
            return res
        return wrapper
    return decor_save_json


def input_csv(path_scv: str):
    """
    Декоратор для считывания коэфицентов csv файла и запуска функции расчета корней квадратного уравнения
    с этими коэфицентами
    :param path_scv: csv файл коэфицентов квадратного уравнения
    :return: словарь
    """
    def decor_run(func: Callable):
        def wrapper(*args):
            result = dict()
            koef_list = load_csv(path_scv)
            for tup in koef_list:
                res = func(*tup)
                key = "_".join(map(str,tup))
                result[key] = res
            return result
        return wrapper
    return decor_run

@output_json(PATH_JSON)
@input_csv(PATH_CSV)
def resolve_quadratic(a: int, b: int, c: int) -> tuple:
    # Вычисляем дискриминант квадратного уравнения
    d = b**2 -4*a*c
    if d < 0:
        return (None)
    elif d == 0:
        return (-b / (2 * a))
    else:
        return (((-b + d**0.5) / (2 * a)), ((-b - d**0.5) / (2 * a)))


if __name__ == "__main__":
    # Сохранение коэфицентов в csv файл
    save_csv(generator_koeficient(100,1,100), PATH_CSV)

    print(resolve_quadratic(1, 4, 2))