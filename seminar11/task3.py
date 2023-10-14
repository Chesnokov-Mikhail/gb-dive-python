# Разработайте программу для работы с прямоугольниками. Необходимо создать класс Rectangle, который будет представлять прямоугольник с заданными шириной и высотой.
# Атрибуты класса:
# width (int): Ширина прямоугольника. height (int): Высота прямоугольника.
# Методы класса:
# __init__(self, width, height=None): Конструктор класса. Принимает ширину и высоту прямоугольника. Если высота не указана (по умолчанию None), то считается, что прямоугольник является квадратом, и высота устанавливается равной ширине.
# perimeter(self): Метод для вычисления периметра прямоугольника. Возвращает целое число - значение периметра.
# area(self): Метод для вычисления площади прямоугольника. Возвращает целое число - значение площади.
# __add__(self, other): Магический метод, который определяет операцию сложения (+) для двух прямоугольников. Принимает другой прямоугольник other. Создает новый прямоугольник, который представляет собой объединение исходных прямоугольников по периметру. Возвращает новый прямоугольник.
# __sub__(self, other): Магический метод, который определяет операцию вычитания (-) одного прямоугольника из другого. Принимает вычитаемый прямоугольник other. Создает новый прямоугольник, представляющий разницу периметров исходных прямоугольников, и вычисляет высоту на основе этой разницы. Возвращает новый прямоугольник.
# __lt__(self, other): Магический метод, который определяет операцию "меньше" (<) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше площади второго, иначе False.
# __eq__(self, other): Магический метод, который определяет операцию "равно" (==) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площади равны, иначе False.
# __le__(self, other): Магический метод, который определяет операцию "меньше или равно" (<=) для двух прямоугольников. Принимает другой прямоугольник other. Возвращает True, если площадь первого прямоугольника меньше или равна площади второго, иначе False.
# __str__(self): Магический метод, возвращающий строковое представление прямоугольника. Возвращает строку, описывающую ширину и высоту прямоугольника.
# __repr__(self): Магический метод, возвращающий строковое представление прямоугольника, которое может быть использовано для создания нового объекта такого же класса с теми же атрибутами.
# Пояснение:
# Метод __add__ объединяет два прямоугольника по периметру и создает новый прямоугольник.
# Метод __sub__ вычитает один прямоугольник из другого, представляя разницу периметров исходных прямоугольников, и создает новый прямоугольник.
# Методы сравнения __lt__, __eq__ и __le__ сравнивают прямоугольники по их площади.
# Методы __str__ и __repr__ предоставляют строковое представление объекта класса Rectangle.
from functools import total_ordering

@total_ordering
class Rectangle:

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Rectangle):
            return ((self.height == o.height) and (self.width == o.width))
        raise TypeError

    def __lt__(self, other) -> bool:
        if isinstance(other, Rectangle):
            return (self.area() < other.area())
        raise TypeError

    def __init__(self, width: int, height: int=None):
        self.width = width
        self.height = height if height else width

    def perimeter(self) -> int:
        return (self.width + self.height) * 2

    def area(self) -> int:
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return Rectangle((self.width + other.width), (self.height + other.height))
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rectangle):
            if not ((height := (self.height - other.height)) <= 0 or (width := (self.width - other.width)) <= 0):
                return Rectangle(width, height)
        raise TypeError

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

if __name__ == "__main__":
    rect1 = Rectangle(4, 5)
    rect2 = Rectangle(3, 3)

    print(rect1)
    print(rect2)

    print(rect1.perimeter())
    print(rect1.area())
    print(rect2.perimeter())
    print(rect2.area())
    rect_sum = rect1 + rect2
    rect_diff = rect1 - rect2

    print(rect_sum)
    print(rect_diff)

    print(rect1 < rect2)
    print(rect1 == rect2)
    print(rect1 <= rect2)

    print(repr(rect1))
    print(repr(rect2))

# Ожидаемый ответ:
#
# Прямоугольник со сторонами 4 и 5
# Прямоугольник со сторонами 3 и 3
# 18
# 20
# 12
# 9
# Прямоугольник со сторонами 7 и 8
# Прямоугольник со сторонами 1 и 2
# False
# False
# False
# Rectangle(4, 5)
# Rectangle(3, 3)