# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
from pathlib import Path

FILE_TYPE = {"video": ("avi", "mp4", "mkv", "wmv"),
             "audio": ("mp3", "wav", "aiif", "mid"),
             "images": ("jpeg", "png", "bmp", "gif", "tiff"),
             "text": ("txt", "doc", "docx"),
}

def sort_file_dir(dir_in: str) -> str:
    """
    Сортирует файлы в исходной директории по директориям в зависимости от расширения
    :param dir_in: Исходная директория, где лежат файлы для сортировки
    :return: текстовый результат сортировки файлов
    """
    path_in = Path.cwd().joinpath(dir_in)
    result = ""
    # Проверяем наличие исходной директории
    if path_in.exists() and path_in.is_dir():
        for dir_out, extention_tuple in FILE_TYPE.items():
            source_files = []
            for ext in extention_tuple:
                source_files = path_in.glob("*." + ext)
                if source_files:
                    # Проверяем наличие директорий для сортировки файлов, при её отсутсвии создаем её
                    path_out = Path.cwd().joinpath(path_in.joinpath(dir_out))
                    if not (path_out.exists() and path_out.is_dir()):
                        path_out.mkdir(parents=True)
                    # перемещаем найденные файлы в сортированную директорию
                    for file in source_files:
                        pass
                        file.replace(path_out.joinpath(file.name))
    else:
        result = f"Исходная директория {path_in} не существует"
    return result

if __name__ == "__main__":
    dir_sorted = ".\\task1_dir"
    result = sort_file_dir(dir_sorted)
    if not result:
        print(f"Файлы в директории {Path.cwd().joinpath(dir_sorted)} успешно отсортированы")
    else:
        print(f"Файлы в директории не отсортированы по причине: {result}")