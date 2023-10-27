# 📌Напишите код, который запускается из командной строки и получает
# на вход путь до директории на ПК.
# 📌Соберите информацию о содержимом в виде объектов namedtuple.
# 📌Каждый объект хранит: ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл, ○ флаг каталога, ○ название родительского каталога.
# 📌В процессе сбора сохраните данные в текстовый файл используя логирование.
import logging
import argparse
from pathlib import Path
from collections import namedtuple

# Задаем формат логера и его конфигурацию
FORMAT = "{levelname:<5} - {msg}"
logging.basicConfig(filename="directory_search.log", filemode="w", encoding="UTF-8", level=logging.INFO,
                    style="{", format=FORMAT)
logger = logging.getLogger(__name__)

def scan_dir(dir: str) -> list:
    """
    В исходной директории формирует список содержимого
    :param dir: исходная директория
    :return: список[namedtuple('Dir_info', ['name'=имя директории или файла без расширения,
                                'extension'=расширение файла, 'directory'=флаг директории,
                                 'parent_directory'=родительская директория])]
    """
    path_dir = Path(dir).resolve()
    dir_list = list()
    # Задаем именованный кортеж нужно структуры
    Dir_info = namedtuple('Dir_info', ['name', 'extension', 'directory', 'parent_directory'])
    # Проверяем наличие исходной директории
    if path_dir.exists() and path_dir.is_dir():
        # обходим рекурсивно все директории и файлы в исходной директории
        # и заполняем список[namedtuple(имя директории или файла без расширения, расширение файла, флаг директории,
        #                               родительская директория)]
        for items in path_dir.rglob("*"):
            if items.is_dir():
                dir_list.append(Dir_info(items.name,'',True,str(items.parent)))
            if items.is_file():
                dir_list.append(Dir_info(items.stem, items.suffix, False, str(items.parent)))
            logger.info(msg=f"name={dir_list[-1].name}, extension={dir_list[-1].extension},"
                            f" directory={dir_list[-1].directory},"
                            f" parent_directory={dir_list[-1].parent_directory}")
        return dir_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument('dir', metavar='patch', type=str, nargs=1, help='Enter the directory path')
    args = parser.parse_args()
    path_dir = args.dir[0]
    dir_info = scan_dir(path_dir)




