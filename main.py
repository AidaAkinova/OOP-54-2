# Класс

def test():
    print("def")

class Hero:

    # Конструктор класса
    def __init__(self, name="John Doe", lvl=1, hp=100):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp

    # Метод класса
    def action(self):
        print(f"self {self}")
        print(f"Базовое действие {self.name}")



# Экзепляр класса| Объект класса
kirito = Hero("Kirito", 100, 1000)
asuna = Hero(hp=1000, name="Asuna", lvl=98)

# test = int()


kirito.action()
asuna.action()

# print(asuna.hp_1)