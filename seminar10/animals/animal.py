class Animals:
    """
    Базовый класс для животных
    """
    def __init__(self, name: str, color: str):
        """
        Инициализация базового класса
        :param name: название животного
        :param color: цвет животного
        """
        self.name = name
        self.color = color