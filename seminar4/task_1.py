" 1. Напишите функцию для транспонирования матрицы"

def matrix_transposition(matrix: list) -> list:
    """Функция транспонирования матрицы"""
    result = [[[] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

def matrix_print(matrix: list) -> None:
    """Печать матрицы построчно"""
    for i in range(len(matrix)):
        print(matrix[i])
    print()

# Ввод матрицы
matrix_ = [[1,2,3,8], [4,5,6,7], [8,9,10,11]]
# Исходная матрица
print("Исходная матрица: ")
matrix_print(matrix_)
# Транспонированная матрица
print("Транспонированная матрица: ")
matrix_print(matrix_transposition(matrix_))