#2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны
# с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
# равнобедренным или равносторонним.

side_a = float(input("Введите длину стороны 'a' треугольника: "))
side_b = float(input("Введите длину стороны 'b' треугольника: "))
side_c = float(input("Введите длину стороны 'c' треугольника: "))

if side_a < (side_c + side_b):
    if side_c < (side_b + side_a):
        if side_b < (side_c + side_a):
            if side_c == side_b == side_a:
                print("треугольник равносторонний")
            elif side_a == side_b or side_c == side_b or side_c == side_a:
                print("треугольник равнобедренный")
            else:
                print("треугольник разносторонний")
        else:
            print("треугольник стакими сторонами не существует")