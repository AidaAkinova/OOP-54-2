class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        print(f"{self.name} выполняет действие!")

    def attack(self):
        print(f"{self.name} атакует!")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        if self.arrows > 0:
            self.arrows -= 1
            import random
            success = random.random() < self.precision
            if success:
                print(f"{self.name} выпустил стрелу и попал в цель! Осталось стрел: {self.arrows}")
            else:
                print(f"{self.name} выпустил стрелу, но промахнулся! Осталось стрел: {self.arrows}")
        else:
            print(f"У {self.name} закончились стрелы!")

    def rest(self):
        self.arrows += 5
        print(f"{self.name} отдохнул и пополнил запас стрел. Теперь у него {self.arrows} стрел.")

    def status(self):
        return f"Имя: {self.name}, Здоровье: {self.hp}, Стрелы: {self.arrows}, Точность: {self.precision * 100}%"

if __name__ == "__main__":
    legolas = Archer("Леголас", 100, 10, 0.8)
    print(legolas.status())
    legolas.action()
    for _ in range(12):
        legolas.attack()
    legolas.rest()
    print(legolas.status())