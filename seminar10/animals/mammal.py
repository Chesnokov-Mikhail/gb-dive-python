from animals import Animals

class Mammal(Animals):
    """
    Класс млекопитающих
    """
    def __init__(self, name: str, color: str, kind: str):
        """
        Создание экземпляра млекопитающего
        :param name: название млекопитающего
        :param color: цвет млекопитающего
        :param kind: вид млекопитающего
        """
        super().__init__(name, color)
        self.kind = kind

    def __str__(self):
        return f"Млекопитающее {self.name} вида {self.kind}"

if __name__ == "__main__":
    anim_1 = Mammal("Барс", "Белый", "Кошачий")
    print(anim_1)
    print(anim_1.__class__.__name__)