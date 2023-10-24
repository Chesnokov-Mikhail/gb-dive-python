# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# 📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# 📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры

import json
from pathlib import Path

# путь к базе хранения пользователей
PATH_DB = "user_db.json"
MIN_LEVEL = 1
MAX_LEVEL = 7

class AccesError(Exception):
    def __init__(self, msg: str):
        self.message = msg

    def __str__(self):
        return f"Исключение доступа к: {self.message}"

class User:
    def __init__(self, name:str, id:int, level:int=MIN_LEVEL):
        try:
            self._validate(name, id, level)
            self.name = name
            self.id = id
            self.level = level
        except ValueError as e:
            print(e)

    def __str__(self):
        return f"Идентификатор: {self.id}, Имя: {self.name}, Уровень: {self.level}"

    def __repr__(self):
        return f"User(name={self.name}, id={self.id}, level={self.level})"

    def __eq__(self, other):
        if isinstance(other,User):
            return all(((self.id == other.id), (self.name == other.name)))
        raise TypeError(f"Сравниваемый объект не является экземпляром класса {User.__name__}")

    def __lt__(self, other) -> bool:
        if isinstance(other,(User)):
            return (self.level < other.level)
        raise TypeError(f"Сравниваемый объект не является экземпляром класса {User.__name__}")

    def _validate(self, name:str, id:int, level:int=MIN_LEVEL):
        if not name or not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        if not (MIN_LEVEL <= level <= MAX_LEVEL):
            raise ValueError(f"введите корректный уровень доступа от {MIN_LEVEL} до {MAX_LEVEL}")
        return True

def load_db() -> dict:
    path = Path(PATH_DB)
    if path.exists() and path.is_file():
        with path.open("r", encoding="UTF-8") as f:
            data = json.load(f)
    else:
        data = dict()
    return data

def save_db(my_dict: dict) -> bool:
    path = Path(PATH_DB)
    with path.open("w", encoding="UTF-8") as f:
        json.dump(my_dict, f, indent=4, ensure_ascii=False)
        return True
    return False

def load_users_from_json() -> list[User]:
    """
    считывает информацию из JSON файла и формирует множество пользователей.
    :param data:
    :return:
    """
    result = list()
    data = load_db()
    for level, user_dict in data.items():
        for id, name in user_dict.items():
            user = User(name, int(id), int(level))
            result.append(user)
    return result

class Logger:
    # список пользователей
    __users = list()
    # список авторизованных пользователей
    __users_log = list()

    def __init__(self):
        self.__users = load_users_from_json()

    def authorize(self, name: str, id: int) -> User:
        user_log = User(name, id)
        for user in self.__users:
            if user_log == user:
                user_log.level = user.level
                self.__users_log.append(user_log)
                return user_log

    def add_user_db(self, my_user: User, other: User) -> bool:
        if my_user in self.__users_log:
            try:
                if other < my_user:
                    raise AccesError(f"Уровень добавляемого пользователя {other.level} меньше вашего уровня {my_user.level}")
            except AccesError as e:
                print(e)
                return False
            else:
                return self.__add_new_user_db(other)
        else:
            print("Вы не авторизованный пользователь")
            return False

    @staticmethod
    def __add_new_user_db(user: User) -> bool:
        users_id = set()
        data = load_db()
        for users in data.values():
            users_id.update(map(int, users.keys()))
        try:
            if user.id in users_id:
                raise ValueError(f"Идентификатор {user.id} существует, измените идентификатор.")
        except ValueError as e:
            print(e)
        else:
            if user.level in map(int, data.keys()):
                data[str(user.level)][user.id] = user.name
            else:
                data[str(user.level)] = {user.id: user.name}
            save_db(data)
            return True
        return False

if __name__ == "__main__":
    loging = Logger()
    user = loging.authorize("Михаил",1)
    print(user)
    user_2 = User("Вова",11,6)
    print(loging.add_user_db(user, user_2))