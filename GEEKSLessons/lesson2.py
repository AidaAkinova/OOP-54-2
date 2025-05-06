#
# # Верблюжая натация
# # Змеиная натация
#
# # WarriorHero
# # warrior_hero
#
# # Наследование
#
# class Person:
#
#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#
#
# # Родительский|Супер класс
# class Hero:
#     def __init__(self, name, lvl, hp):
#         self.name = name
#         self.lvl = lvl
#         self.hp = hp
#
#     def introduce(self):
#         return print(f"Я {self.name}, мой уровень {self.lvl}")
#
#     def action(self):
#         return print(f"{self.name} выполняет базовое действие!!")
#
# hero = Hero("Hero", 100, 100)
#
#
# # Дочерний класс
# class MageHero(Hero):
#
#     def __init__(self, name, lvl, hp, mp):
#         super().__init__(name, lvl, hp)
#         self.mp = mp
#
#     def cast_spell(self):
#         return print(f"Кастую огонь")
#
#     def action(self):
#         return print(f"{self.name} ничего не делает!!")
#
#
#
# mage_hero = MageHero("Маг", 100, 100, 1000)
#
# mage_hero.action()



class Animal:
    def action(self):
        return print("Animal action")


class Swim(Animal):

    def action(self):
        super().action()
        # return print("Swim action")

class Fly(Animal):

    def action(self):
        super().action()
        # return print(f"Fly action")

# MRO ( Method Resolution Order )
class Duck(Fly, Swim):
    pass


donald_duck = Duck()

donald_duck.action()

print(Duck.mro())