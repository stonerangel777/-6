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


class Lecturer(Person):
    def __init__(self, name, family, age, nationality, university, experience):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.experience = experience

    def print(self):
        super().print()
        print("Университет:", self.university)
        print("Преподавателски стаж:", self.experience, "години")


# Създаване на обекти
lecturer1 = Lecturer("Петър", "Петров", 45, "Българин",
                     "Софийски университет", 15)

lecturer2 = Lecturer("Елена", "Иванова", 50, "Българка",
                     "Технически университет", 20)

# Извикване на метода print()
lecturer1.print()
print()
lecturer2.print()