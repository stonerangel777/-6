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


class Student(Person):
    def __init__(self, name, family, age, nationality, university, yearofstudy):
        super().__init__(name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print(self):
        super().print()
        print("Университет:", self.university)
        print("Година на обучение:", self.yearofstudy)


# Създаване на обекти
student1 = Student("Георги", "Георгиев", 20, "Българин",
                   "Софийски университет", 2)

student2 = Student("Анна", "Димитрова", 22, "Българка",
                   "Технически университет", 4)

# Извикване на метода print()
student1.print()
print()
student2.print()