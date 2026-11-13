class Person:
    def __init__(self, name, family, age, nationality):
        self.name = name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print(self):
        print("Име:", self.name)
        print("Фамилия:", self.family)
        print("Възраст:", self.age)
        print("Националност:", self.nationality)


# Създаване на обекти
person1 = Person("Иван", "Иванов", 25, "Българин")
person2 = Person("Maria", "Petrova", 30, "Bulgarian")

# Извикване на метода print()
person1.print()
print()
person2.print()