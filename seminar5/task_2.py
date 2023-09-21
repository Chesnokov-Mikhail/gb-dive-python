# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os
def info_file(path_file: str) -> tuple:
    """
    Извлекает из абсолютного пути до файла, путь, имя файла, расширение файла.
    :param path_file: абсолютный путь до файла
    :return: кортеж элементов: путь, имя файла, расширение файла.
    """
    # Устанавливаем символ разделителя пути файловой системы в зависимости от операционной системы
    sep = "/"
    if os.name == "nt":
        sep = "\\"
    path = path_file.split(sep)
    file = path[-1:][0]
    file_extension = file.split(".")[-1:][0] if len(file.split(".")) > 1 else ""
    file_name = ".".join(file.split(".")[:-1]) if len(file.split(".")) > 1 else file
    path = sep.join(path[:-1])
    return (path,file_name,file_extension)

def main():
    str_ = input("Введите абсолютный путь до файла: ")
    print(info_file(str_))

if __name__ == "__main__":
    main()