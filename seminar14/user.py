import json
from pathlib import Path

# путь к базе хранения пользователей
PATH_DB = "user_db.json"
# минимальный и максимальный уровень доступа
MIN_LEVEL = 1
MAX_LEVEL = 7

class AccesError(Exception):
    """
    Исключение уровня доступа
    """
    def __init__(self, msg: str):
        self.message = msg

    def __str__(self):
        return f"Исключение доступа к: {self.message}"

class User:
    """
    Класс пользователя, устанавливается имя пользователя, его уникальный идентификатор и уровень доступа,
    """
    def __init__(self, name:str, id:int, level:int=MAX_LEVEL):
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
        """
        метод сравнения пользователей. Пользователи равны если равны идентификаторы и имена
        :param other: сравниваемый пользователь
        :return: bool или исключение если передан для сравнения экземпляр не класса User
        """
        if isinstance(other,User):
            return all(((self.id == other.id), (self.name == other.name)))
        raise TypeError(f"Сравниваемый объект не является экземпляром класса {User.__name__}")

    def __lt__(self, other) -> bool:
        """
        метод сравнения пользователей на меньше. Пользователь меньше, если его уровень меньше
        уровня сравниваемого пользователя
        :param other: сравниваемый пользователь
        :return: bool или исключение если передан для сравнения экземпляр не класса User
        """
        if isinstance(other,(User)):
            return (self.level < other.level)
        raise TypeError(f"Сравниваемый объект не является экземпляром класса {User.__name__}")

    def _validate(self, name:str, id:int, level:int=MIN_LEVEL):
        """
        метод валидации параметров инициализации
        :param name: имя пользователя
        :param id: уникальный идентификатор пользователя
        :param level: уровень доступа пользователя
        :return: bool
        """
        if not name or not name.isalpha():
            raise ValueError('Имя должно быть текстового вида')
        if not (MIN_LEVEL <= level <= MAX_LEVEL):
            raise ValueError(f"введите корректный уровень доступа от {MIN_LEVEL} до {MAX_LEVEL}")
        if id < 0:
            raise ValueError('Идентификатор должен быть положительным числом')
        return True

def load_db() -> dict:
    """
    загрузка базы пользователей из JSON
    :return: словарь пользователей {level: {id: name}}
    """
    path = Path(PATH_DB)
    if path.exists() and path.is_file():
        with path.open("r", encoding="UTF-8") as f:
            data = json.load(f)
    else:
        data = dict()
    return data

def save_db(my_dict: dict) -> bool:
    """
    сохранение словаря пользователей в JSON
    :param my_dict: словарь пользователей {level: {id: name}}
    :return: bool
    """
    path = Path(PATH_DB)
    with path.open("w", encoding="UTF-8") as f:
        json.dump(my_dict, f, indent=4, ensure_ascii=False)
        return True
    return False

def load_users_from_json() -> list[User]:
    """
    считывает информацию из JSON файла и формирует спиок пользователей как экземпляры класса User.
    :return: список пользователей [User]
    """
    result = list()
    data = load_db()
    for level, user_dict in data.items():
        for id, name in user_dict.items():
            user = User(name, int(id), int(level))
            result.append(user)
    return result

class Logger:
    """
    Класс логирования с авторизацией пользователей по базе пользователей
    """
    # список пользователей
    __users = list()
    # список авторизованных пользователей
    __users_log = list()

    def __init__(self):
        self.__users = load_users_from_json()

    def authorize(self, name: str, id: int) -> User:
        """
        Метод авторизации пользователя.
        :param name: имя пользователя
        :param id: идентификатор пользователя
        :return:Если авторизация успешна, то возвращается пользователь с
        установленным уровнем доступа или None
        """
        user_log = User(name, id)
        for user in self.__users:
            if user_log == user:
                user_log.level = user.level
                self.__users_log.append(user_log)
                return user_log

    def add_user_db(self, my_user: User, other: User) -> bool:
        """
        метод добавления авторизованным пользователем других пользователя в базу пользователей
        :param my_user: аторизованный пользователь
        :param other: добавляемый пользователь
        :return: bool
        """
        if my_user in self.__users_log:
            # try:
            #     if other < my_user:
            #         raise AccesError(f"Уровень добавляемого пользователя {other.level} меньше вашего уровня {my_user.level}")
            # except AccesError as e:
            #     print(e)
            #     return False
            if other < my_user:
                raise AccesError(f"Уровень добавляемого пользователя {other.level} меньше вашего уровня {my_user.level}")
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
    user_3 = loging.authorize("Михаил", 23)
    print(user_3)
    user_2 = User("Вова",11,6)
    print(loging.add_user_db(user, user_2))
    user_4 = User("213sd", 3, 3)