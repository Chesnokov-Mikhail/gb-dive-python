import json
import csv
from pathlib import Path

def save_json(data_dict: dict, path_json: str) -> bool:
    """
    Сохраняет словарь в JSON формате
    :param data_dict: словарь
    :path_json: путь к JSON файлу
    :return: в случае успешного сохранения True, иначе False
    """
    path = Path(path_json)
    if path.parent.exists():
        with path.open("w", encoding="UTF-8") as f:
            json.dump(data_dict, f, indent=4)
        return True
    return False

def save_csv(array_tuple: list[tuple[int, int, int]], path_csv: str) -> bool:
    """
    Сохраняет массив [(int,int,int)] в CSV формате, разделитель табуляция
    :param array_tuple: массив [(int,int,int)]
    :path_csv: путь к CSV файлу
    :return: в случае успешного сохранения True, иначе False
    """
    path = Path(path_csv)
    if path.parent.exists():
        with path.open("w", newline="", encoding="UTF-8") as f:
            csv_write = csv.writer(f, dialect='excel-tab', quoting=csv.QUOTE_MINIMAL)
            csv_write.writerows(array_tuple)
        return True
    return False

def load_csv(path_csv: str) -> list[tuple[int, int, int]]:
    """
    Считывает данные из csv файла
    :param path_csv: путь к CSV файлу
    :return: в случае успешного сохранения True, иначе False
    """
    array_tuple = list()
    path = Path(path_csv)
    if path.parent.exists():
        with path.open("r", newline="", encoding="UTF-8") as f:
            csv_reader = csv.reader(f, dialect='excel-tab', quoting=csv.QUOTE_MINIMAL)
            for item in csv_reader:
                array_tuple.append(tuple(map(int,item)))
    return array_tuple