# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.
#2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

class Triangle:
    """
    Класс треугольников
    """
    # типы треугольников
    __TYPE_TRIANGLE = {"EQUILATERAL_TRIANGLE": "треугольник равносторонний",
                     "ISOSCELES_TRIANGLE": "треугольник равнобедренный",
                     "SCALENE_TRIANGLE": "треугольник разносторонний",}

    def __str__(self) -> str:
        return f"{Triangle.__TYPE_TRIANGLE[self.__type]} со сторонами side_a = {self.side_a}, side_b = {self.side_b}, side_c = {self.side_c},"

    @staticmethod
    def __check_enable(side_a: float, side_b: float, side_c: float) -> str:
        """
        Проверка существования треугольника и определение его типа
        :param side_a: сторона а треугольника
        :param side_b: сторона b треугольника
        :param side_c: сторона c треугольника
        :return: тип треуголиника
        """
        result = str()
        if side_a < (side_c + side_b):
            if side_c < (side_b + side_a):
                if side_b < (side_c + side_a):
                    if side_c == side_b == side_a:
                        result = "EQUILATERAL_TRIANGLE"
                    elif side_a == side_b or side_c == side_b or side_c == side_a:
                        result = "ISOSCELES_TRIANGLE"
                    else:
                        result = "SCALENE_TRIANGLE"
        return result

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        type_triangle = Triangle.__check_enable(side_a, side_b, side_c)
        if type_triangle:
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
            self.__type = type_triangle

    def set_side_a(self, side_a: float) -> bool:
        """
        изменение стороны a треугольника
        :param side_a: сторона a
        :return: True если изменения стороны возможны, в противном случае False
        """
        if type_triangle := Triangle.__check_enable(side_a, self.side_b, self.side_c):
            self.side_a = side_a
            self.__type = type_triangle
            return True
        else:
            return False

    def set_side_b(self, side_b: float) -> bool:
        """
        изменение стороны b треугольника
        :param side_a: сторона b
        :return: True если изменения стороны возможны, в противном случае False
        """
        if type_triangle := Triangle.__check_enable(self.side_a, side_b, self.side_c):
            self.side_b = side_b
            self.__type = type_triangle
            return True
        else:
            return False

    def set_side_c(self, side_c: float) -> bool:
        """
        зменение стороны c треугольника
        :param side_a: сторона c
        :return: True если изменения стороны возможны, в противном случае False
        """
        if type_triangle := Triangle.__check_enable(self.side_a, self.side_b, side_c):
            self.side_c = side_c
            self.__type = type_triangle
            return True
        else:
            return False

    def get_type_triangle(self) -> str:
        """
        возвращает тип экземпляра треугольника
        :return: ["EQUILATERAL_TRIANGLE", "ISOSCELES_TRIANGLE", "SCALENE_TRIANGLE"]
        """
        return self.__type

    def enable(self) -> bool:
        """
        проверяет установлены ли экземпляру треугольника атрибуты
        :return: True если установлены атрибуты, в противном случае False
        """
        return True if self.__dict__ else False

if __name__ == "__main__":
    triangl_1 = Triangle(4,4,8)
    if triangl_1.enable():
        print(triangl_1)
    else:
        print("Треугольник не существует")
    triangl_2 = Triangle(5, 4, 5)
    if triangl_2.enable():
        print(triangl_2)
    else:
        print("Треугольник не существует")