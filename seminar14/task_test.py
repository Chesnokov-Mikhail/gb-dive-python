# 📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень)
# 📌 Напишите 3-7 тестов pytest (или unittest на ваш выбор) для данного проекта
# 📌 ОБЯЗАТЕЛЬНО! Используйте фикстуры

import pytest
from user import User, Logger, save_db, AccesError

@pytest.fixture
def data_users():
    """
    исходная база пользователей для тестирования
    :return:
    """
    users_dict = {1: {0: "Администратор"},
            6: {
                12: "Михаил",
                11: "Вова"
            },
            5: {
                2: "Юрий",
                4: "Николай"
            },
            4: {
                3: "Циля"
            },
            }
    save_db(users_dict)

@pytest.fixture
def god_user():
    return User("Администратор", 0, 1)

@pytest.fixture
def good_user():
    return User("Вова", 11, 6)

@pytest.fixture
def bad_user():
    return User("Александр", 1, 3)

def test_bad_create_user(capfd):
    """
    тестирование создания пользователя с ошибкой в имени
    :param capfd: фикстура (capture ﬁle descriptors)
    :return:
    """
    User("213sd", 3, 3)
    captured = capfd.readouterr()
    assert captured.out == 'Имя должно быть текстового вида\n'

def test_create_user(good_user):
    """
    тестирование удачного создание пользователя
    :param good_user: имеющийся пользователь из базы
    :return:
    """
    assert User(good_user.name, good_user.id, good_user.level) == good_user

def test_good_autorized(data_users, good_user):
    """
    тестирование удачной авторизации
    :param data_users: база пользователей
    :param good_user: имеющийся пользователь из базы
    :return:
    """
    loging = Logger()
    assert good_user == loging.authorize(good_user.name, good_user.id)

def test_bad_autorized(data_users,bad_user):
    """
    тестирование неудачной авторизации
    :param data_users: база пользователей
    :param bad_user: пользователькоторого нет в базе
    :return:
    """
    loging = Logger()
    assert None == loging.authorize(bad_user.name, bad_user.id)

def test_bad_add_user(capfd, data_users, good_user, god_user):
    """
    тестирование добавление пользователя не с уникальным идентификатором
    :param data_users: база пользователей
    :param good_user: имеющийся пользователь в базе
    :return:
    """
    loging = Logger()
    user = loging.authorize(god_user.name, god_user.id)
    loging.add_user_db(user, good_user)
    captured = capfd.readouterr()
    assert captured.out == f"Идентификатор {good_user.id} существует, измените идентификатор.\n"

def test_not_acces_add_user(data_users, bad_user, good_user):
    """
    тестирование ошибки добавления пользователя с меньшим уровнем доступа
    :param data_users: база пользователей
    :param bad_user: добавляемы пользователь с меньшим уровнем
    :param good_user: имеющийся пользователь в базе с большим уровнем
    :return:
    """
    loging = Logger()
    user = loging.authorize(good_user.name, good_user.id)
    with pytest.raises(AccesError, match=f"Исключение доступа к: Уровень добавляемого пользователя {bad_user.level} меньше вашего уровня {user.level}"):
        loging.add_user_db(user, bad_user)

def test_bad_id_add_user(capfd, data_users, good_user):
    """
    тестирование добавление пользователя не с уникальным идентификатором
    :param data_users: база пользователей
    :param good_user: имеющийся пользователь в базе

    :return:
    """
    loging = Logger()
    user = loging.authorize("Администратор", 0)
    loging.add_user_db(user, good_user)
    captured = capfd.readouterr()
    assert captured.out == f"Идентификатор {good_user.id} существует, измените идентификатор.\n"

if __name__ == '__main__':
    pytest.main(['-v'])