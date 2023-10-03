# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
#    файлов в ней с учётом всех вложенных файлов и директорий.

# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет  для работы с файлами разных форматов.

from save_file import save_json,save_csv,save_pickle
from pathlib import Path

PATH_DB_JSON = ".\scan_dir_db.json"
PATH_DB_CSV = ".\scan_dir_db.csv"
PATH_DB_PICKLE = ".\scan_dir_db.pickle"

def calculate_size_dir(dirs_dict: dict, root: str) -> int:
    """
    Функция рекурсивно подсчитывает размер вложенных в директорию файлов
    :param dirs_dict: словарь {родительская директория : [имя объекта, файл/директория, размер]}
    :param root: родительская директория, размер которой подсчитывается
    :return: размер директории в байтах
    """
    size = 0
    if dirs_dict.get(root, False):
        for items in dirs_dict[root]:
            if items[1] == "file":
                size += items[2]
            else:
                size += calculate_size_dir(dirs_dict, str(Path(root).joinpath(items[0])))
    return size

def scan_dir(dir: str) -> dict:
    """
    В исходной директории формирует словарь вложенных директорий и файлов
    :param dir: исходная директория
    :return: словарь {родительская директория : [имя объекта, файл/директория, размер]}
    """
    path_dir = Path(dir).resolve()
    dict_items = dict()
    # Проверяем наличие исходной директории
    if path_dir.exists() and path_dir.is_dir():
        # обходим рекурсивно все директории и файлы в исходной директории
        # и заполняем словарь {родительская директория : [имя объекта, файл/директория, размер]}
        for items in path_dir.rglob("*"):
            if items.is_dir():
                dict_items.setdefault(str(items.parent),[])
                item = [items.name, "directory",0]
                dict_items[str(items.parent)].append(item)
            if items.is_file():
                dict_items.setdefault(str(items.parent),[])
                item = [items.name, "file",items.stat().st_size]
                dict_items[str(items.parent)].append(item)
        # расчитываем размер директорий
        for root, items in dict_items.items():
            for item in items:
                if item[1] == "directory":
                    item[2] = calculate_size_dir(dict_items, str(Path(root).joinpath(item[0])))
        return dict_items

if __name__ == "__main__":
    path_dir = input("Введите путь к директории для обхода ей вложений: ")
    dir_info = scan_dir(path_dir)
    if save_json(dir_info,PATH_DB_JSON):
        print(f"Результат сохранен в формата JSON в файле: {Path(PATH_DB_JSON).resolve()}")
    else:
        print(f"Результат НЕ сохранен в файле: {Path(PATH_DB_JSON).resolve()}")
    if save_pickle(dir_info,PATH_DB_PICKLE):
        print(f"Результат сохранен с помощью модуля pickle в файле: {Path(PATH_DB_PICKLE).resolve()}")
    else:
        print(f"Результат НЕ сохранен в файле: {Path(PATH_DB_PICKLE).resolve()}")
    if save_csv(dir_info,PATH_DB_CSV):
        print(f"Результат сохранен в формата CSV в файле: {Path(PATH_DB_CSV).resolve()}")
    else:
        print(f"Результат НЕ сохранен в формата CSV в файле: {Path(PATH_DB_CSV).resolve()}")