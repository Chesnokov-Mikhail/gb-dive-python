# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
import animals

class Fabric_animals:
    """
    Класс-фабрика для создания дочерних классов Animals
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def create_animal(name_animals_class: str, *args, **kwargs) -> animals.Animals:
        """
        статический метод (нет необходимости в передачи экземпляра класса) для создания дочерних классов Animals
        :param name_animals_class: имя класса
        :param args: позиционные параметры создания класса
        :param kwargs: именные параметры создания класса
        :return: дочерний класс Animals
        """
        result = None
        match name_animals_class:
            case animals.Bird.__name__:
                result = animals.Bird(*args, **kwargs)
            case animals.Fish.__name__:
                result = animals.Fish(*args, **kwargs)
            case animals.Mammal.__name__:
                result = animals.Mammal(*args, **kwargs)
        return result

if __name__ == "__main__":
    fab = Fabric_animals()
    bird_1 = fab.create_animal("Bird", "Ворон", "Black", True, True)
    print(bird_1.__class__.__name__)