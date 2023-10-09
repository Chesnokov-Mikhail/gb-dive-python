# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
# 1. Напишите функцию для транспонирования матрицы"

class MatrixUser:

    def __init__(self, matrix: list[list]):
        self.value = matrix

    def transposition(self):
        """
        Функция транспонирования матрицы
        :return: экземпляр класса с транспонированной матрицей
        """
        result = [[[] for j in range(len(self.value))] for i in range(len(self.value[0]))]
        for i in range(len(self.value)):
            for j in range(len(self.value[0])):
                result[j][i] = self.value[i][j]
        return MatrixUser(result)

    def __str__(self):
        """
        Печать матрицы построчно
        :return:
        """
        result = ""
        for i in range(len(self.value)):
            result += f"{self.value[i]}\n"
        return result

if __name__ == "__main__":
    # Ввод матрицы
    matrix_ = MatrixUser([[1,2,3,8], [4,5,6,7], [8,9,10,11]])
    # Исходная матрица
    print("Исходная матрица: ")
    print(matrix_)
    # Транспонированная матрица
    print("Транспонированная матрица: ")
    print(matrix_.transposition())