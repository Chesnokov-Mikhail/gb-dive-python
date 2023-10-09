from animals import Animals

class Bird(Animals):
    """
    Класс птицы
    """
    def __init__(self, name: str, color: str, home: bool, fly: bool):
        """
        Создание экземпляра птицы
        :param name: название птицы
        :param color: цвет птицы
        :param home: домашняя/дикая птица (True/False)
        :param fly: может летать/не летает (True/False)
        """
        super().__init__(name, color)
        self.home = home
        self.fly = fly

    def __str__(self):
        return f"Птица {self.name} является: {'домашней' if {self.home} else 'дикой' };\n" \
               f"{'может летать' if {self.fly} else 'не может летать' };\n" \
               f"цвет: {self.color}"

    def set_flying(self, fly: bool):
        self.fly = fly

    def get_flying(self):
        return self.fly