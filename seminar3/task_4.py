#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

MAX_CAPACITY_BACKPACK = 20
things_hike = {"палатка": 5,
               "спальный мешок": 2,
               "котелок": 2,
               "топор": 2,
               "спички": 1,
               "консервы": 8,
               "крупы": 3,
               "сковородка": 1,
               "ручная пила":1,
               "фонарики":1,
               "тренога для костра":2,
               }

# Список допустимых вещей в рюкзаке
things_backpack = list()

# сортируем словарь по значению от большего к меньшему и получаем соответствующие сортированные ключи
sorted_key_things_hike = sorted(things_hike,key=things_hike.get,reverse=True)
weight_backpack = 0
print(f"Список допустимых вещей в рюкзаке, с максимальной массой {MAX_CAPACITY_BACKPACK} кг.:")
for key in sorted_key_things_hike:
    if (weight_backpack + things_hike[key]) <= MAX_CAPACITY_BACKPACK:
        things_backpack.append(key)
        weight_backpack += things_hike[key]
        print(f" - {key}: {things_hike[key]} кг.")