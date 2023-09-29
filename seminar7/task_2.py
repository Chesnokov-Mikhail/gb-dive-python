# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
from pathlib import Path
def group_files_rename(dir_files: str, in_ext: str, out_ext: str,
                       slice_name: tuple[int,int], desire_name="", serial_digits=3) -> int:
    """
    Переименовывает в директории все файлы с заданным расширением и по шаблону: по срезуберутся буквы из исходного имени файла
    к ним прибавляется желаемое конечное имя, далее счётчик файлов и расширение.
    :param dir_files: директория где переименовываются файлы
    :param in_ext: расширение исходных файлов
    :param out_ext: расширение переименованных файлов
    :param slice_name: срез в имени исходных файлов, начиная с 1, пример (1, 2)
    :param desire_name: название, добавляемой к срезу имени исходного файла
    :param serial_digits: количество цифр в счетчике файла
    :return:
    """
    # Счетчик нумерации файлов
    count_files = 0
    # Проверка диапазона сохраняемого оригинального имени файла
    if slice_name[0] == 0 or slice_name[0] > slice_name[1]:
        return count_files
    path_dir = Path(dir_files)
    # Проверяем наличие исходной директории
    if path_dir.exists() and path_dir.is_dir():
        source_files = path_dir.glob("*." + in_ext)
        if source_files:
            for file in source_files:
                count_files += 1
                name_file = file.stem
                count_name = str(count_files).zfill(serial_digits)
                new_name = name_file[(slice_name[0] - 1):(slice_name[1] + 1)] + desire_name + count_name + "." + out_ext
                file.rename(path_dir.joinpath(new_name))
    return count_files

if __name__ == "__main__":
    dir_rename = ".\\task2_dir"
    slice = (1,4)
    in_ext = "txt"
    new_name = "_new"
    out_ext = "qqq"
    serial_digits = 5
    count_files = group_files_rename(dir_rename, in_ext, out_ext,slice, new_name, serial_digits)
    print(f"Переименовано {count_files} файлов с раширением {in_ext} в директории {Path(dir_rename).resolve()}")