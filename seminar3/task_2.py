#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

lst = [1, 1, "tttt", 5, 7, 3, 9, 33, 5, 6, 7, 55, 55, 3, "tttt", 3]
result = list()

set_lst = set(lst)

for item in set_lst:
    if lst.count(item) >= 2:
        result.append(item)

print(f"Список с дублирующимися элементами: {result}")