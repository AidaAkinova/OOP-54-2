class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, мой возраст {self.age}, мой город {self.city}")

    def is_adult(self):
        return self.age >= 18


person1 = Person("Аида", 25, "Бишкек")
person2 = Person("Айбийке", 5, "Балыкчы")


print(person1.is_adult())
print(person2.is_adult())