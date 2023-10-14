# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
# Атрибуты класса:
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
# Методы класса:
# __init__(self, rows, cols): Конструктор класса, который инициализирует атрибуты rows и cols, а также создает двумерный список data размером rows x cols и заполняет его нулями.
# __str__(self): Метод, возвращающий строковое представление матрицы. Возвращаемая строка представляет матрицу, где элементы разделены пробелами, а строки разделены символами новой строки. Например:
# __repr__(self): Метод, возвращающий строковое представление объекта, которое может быть использовано для создания нового объекта того же класса с такими же размерами и данными.
# __eq__(self, other): Метод, определяющий операцию "равно" для двух матриц. Сравнивает две матрицы и возвращает True, если они имеют одинаковое количество строк и столбцов, а также все элементы равны. Иначе возвращает False.
# __add__(self, other): Метод, определяющий операцию сложения двух матриц. Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов). Если размеры совпадают, создает новую матрицу, где каждый элемент равен сумме соответствующих элементов входных матриц.
# __mul__(self, other): Метод, определяющий операцию умножения двух матриц. Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице. Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.

class Matrix:

    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.data = list([list([0 for i in range(cols)]) for j in range(rows)])

    def __str__(self):
        result = ""
        for i in range(self.rows):
            result += ' '.join(map(str, self.data[i])) + ("\n" if i != (self.rows - 1) else '')
        return result

    def __repr__(self):
        return f"Matrix({self.rows}, {self.cols}, {self.data})"

    def __eq__(self, other) -> bool:
        result = False
        if isinstance(other, Matrix):
            if (self.cols == other.cols) and (self.rows == other.rows) and (self.data == other.data):
                result = True
        return result

    def __add__(self, other):
        if isinstance(other, Matrix):
            if (self.cols == other.cols) and (self.rows == other.rows):
                result = Matrix(self.rows, self.cols)
                result.data = list([list([sum(item) for item in zip(self.data[i], other.data[i])]) for i in range(self.rows)])
                return result
        raise TypeError

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if (self.cols == other.rows):
                result = Matrix(self.rows, other.cols)
                for i in range(self.rows):
                    for j in range(other.cols):
                        result.data[i][j] = sum([self.data[i][r] * other.data[r][j] for r in range(self.cols)])
                return result
        if isinstance(other, (int, float)):
            result = Matrix(self.rows, self.cols)
            for i in range(self.rows):
                for j in range(self.cols):
                    result.data[i][j] = self.data[i][j] * other
            return result
        raise TypeError

if __name__ == "__main__":
    # Создаем матрицы
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    # Выводим матрицы
    print(matrix1)
    print(matrix2)

    # Сравниваем матрицы
    print(matrix1 == matrix2)

    # Выполняем операцию сложения матриц
    matrix_sum = matrix1 + matrix2
    print(matrix_sum)

    # Выполняем операцию умножения матриц
    matrix3 = Matrix(3, 2)
    matrix3.data = [[1, 2], [3, 4], [5, 6]]

    matrix4 = Matrix(2, 2)
    matrix4.data = [[7, 8], [9, 10]]

    result = matrix3 * matrix4
    print(result)

# Ожидаемый ответ:
#
# 1 2 3
# 4 5 6
# 7 8 9
# 10 11 12
# False
# 8 10 12
# 14 16 18
# 25 28
# 57 64
# 89 100
