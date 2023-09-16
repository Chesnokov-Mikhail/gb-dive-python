#Три друга взяли вещи в поход. Сформируйте
#словарь, где ключ — имя друга, а значение —
#кортеж вещей. Ответьте на вопросы:
#✔ Какие вещи взяли все три друга
#✔ Какие вещи уникальны, есть только у одного друга
#✔ Какие вещи есть у всех друзей кроме одного
#и имя того, у кого данная вещь отсутствует
#✔ Для решения используйте операции
#с множествами. Код должен расширяться
#на любое большее количество друзей.

hike = {"Алексей": ("рюкзак", "палатка", "спальный мешок", "котелок", "топор", "спички", "консервы", "удочка"),
        "Михаил": ("рюкзак", "палатка", "спальный мешок", "спички", "крупы", "сковородка"),
        "Сергей": ("рюкзак", "палатка", "спальный мешок", "ручная пила", "фонарики", "тренога для костра"),
        "Альберт": ("рюкзак", "спальный мешок", "ручная пила", "фонарик", "спички"),
        }

#вещи взяли все друзья
same_things = set()
#вещи уникальны, есть только у одного друга
unique_things = set()
#имя друга, у которого отсутствует вещь, которая есть у всех остальных друзей
friend_missing_things = dict()

for key, value in hike.items():
        if not same_things:
                same_things = set(value)
        else:
                same_things = same_things.intersection(value)
        if not unique_things:
                unique_things = set(value)
        else:
                unique_things = (unique_things.symmetric_difference(value)).difference(same_things)
        # вещи есть у всех друзей кроме одного
        same_things_not_one = set()
        for key2, value2 in hike.items():
                if not key2 == key:
                        if not same_things_not_one:
                                same_things_not_one = set(value2)
                        else:
                                same_things_not_one = same_things_not_one.intersection(value2)
        friend_missing_things[key] = same_things_not_one.difference(value)

print(f"Эти вещи взяли все друзья: {same_things}")
print(f"Эти вещи уникальны, есть только у одного друга: {unique_things}")
print(f"Имя друга и отсутствующая вещь, которая есть у всех остальных друзей:")
for key, value in friend_missing_things.items():
        if value:
                print(f"  {key}: {value}")