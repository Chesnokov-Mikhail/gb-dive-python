import json
import pickle
import csv
from pathlib import Path

def save_json(dir_dict: dict, path_json: str) -> bool:
    """
    Сохраняет словарь {родительская директория : [имя объекта, файл/директория, размер]}
    в JSON формате
    :param dir_dict: словарь {родительская директория : [имя объекта, файл/директория, размер]}
    :path_json: путь к JSON файлу
    :return: в случае успешного сохранения True, иначе False
    """
    path = Path(path_json)
    if path.parent.exists():
        with path.open("w", encoding="UTF-8") as f:
            json.dump(dir_dict, f)
        return True
    return False

def save_csv(dir_dict: dict, path_csv: str) -> bool:
    """
    Сохраняет словарь {родительская директория : [имя объекта, файл/директория, размер]}
    в CSV формате с колонками ["root_dir", "name", "file/directory", "size"], разделитель табуляция
    :param dir_dict: словарь {родительская директория : [имя объекта, файл/директория, размер]}
    :path_csv: путь к CSV файлу
    :return: в случае успешного сохранения True, иначе False
    """
    path = Path(path_csv)
    if path.parent.exists():
        with path.open("w", newline="", encoding="UTF-8") as f:
            csv_write = csv.DictWriter(f, fieldnames=["root_dir", "name", "file/directory", "size"],
                                       dialect='excel-tab',
                                       quoting=csv.QUOTE_ALL)
            csv_write.writeheader()
            line = {}
            for key, values in dir_dict.items():
                line["root_dir"] = key
                for value in values:
                    line["name"] = value[0]
                    line["file/directory"] = value[1]
                    line["size"] = value[2]
                    csv_write.writerow(line)
        return True
    return False

def save_pickle(dir_dict: dict, path_pickle: str) -> bool:
    """
    Сохраняет словарь {родительская директория : [имя объекта, файл/директория, размер]} с помощью модуля
    pickle
    :param dir_dict: словарь {родительская директория : [имя объекта, файл/директория, размер]}
    :path_pickle: путь к файлу pickle
    :return: в случае успешного сохранения True, иначе False
    """
    path = Path(path_pickle)
    if path.parent.exists():
        with path.open("wb") as f:
            pickle.dump(dir_dict, f)
        return True
    return False
