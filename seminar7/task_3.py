# Соберите из созданных на уроке и в рамках домашнего задания функций пакет  для работы с файлами.
import files_utils
from pathlib import Path

if __name__ == "__main__":
    dir_rename = ".\\task2_dir"
    slice = (1, 4)
    in_ext = "txt"
    new_name = "_new"
    out_ext = "qqq"
    serial_digits = 5
    count_files = files_utils.group_files_rename(dir_rename, in_ext, out_ext, slice, new_name, serial_digits)
    print(f"Переименовано {count_files} файлов с раширением {in_ext} в директории {Path(dir_rename).resolve()}")
    print()
    dir_sorted = ".\\task1_dir"
    result = files_utils.sort_file_dir(dir_sorted)
    if not result:
        print(f"Файлы в директории {Path(dir_sorted).resolve()} успешно отсортированы")
    else:
        print(f"Файлы в директории не отсортированы по причине: {result}")