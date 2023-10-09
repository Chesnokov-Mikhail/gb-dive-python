from animals import Animals

class Fish(Animals):
    """
    класс рыб
    """
    def __init__(self, name: str, color: str, sea: bool):
        """
        создание экземпляра рыбы
        :param name: название рыбы
        :param sea: морская/пресноводная (True/False)
        """
        super().__init__(name, color)
        self.sea = sea

    def __str__(self):
        return f"Рыба {self.name} является {'морской' if {self.sea} else 'пресноводной' }"