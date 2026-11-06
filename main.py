class Person:
    def __init__(self, name, birth_day, occupation, higher_education):
        self.name = name
        self.birthday = birth_day
        self.occupation = occupation
        self.education = higher_education

    def introduce(self):
        print(
            f"Меня зовут {self.name}, я родился(лась) {self.birthday}, "
            f"по профессии {self.occupation}, "
            f"высшее образование: {self.education}"
        )


class Classmate(Person):
    def __init__(self, name, birth_day, occupation, higher_education, group_name):
        super().__init__(name, birth_day, occupation, higher_education)
        self.group_name = group_name

    def introduce(self):
        super().introduce()
        print(f"Я одногруппник Байэля, " f"наша группа называется {self.group_name}")


class Friend(Person):
    def __init__(self, name, birth_day, occupation, higher_education, hobby):
        super().__init__(name, birth_day, occupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        super().introduce()
        print(f"Моё хобби: {self.hobby}")


class BestFriend(Friend):
    def __init__(
        self, name, birth_day, occupation, higher_education, hobby, shared_memory
    ):
        super().__init__(name, birth_day, occupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        super().introduce()
        print(f"Наша общая история: {self.shared_memory}")


person = Person("Kurmanbek", "17.10.2009", "ещё нет", "учусь")

friend = Friend("Dastan", "24.05.2010", "ещё нет", "есть", "рыбалка")

friend1 = Friend("Abadan", "17.06.2006", "Повар", "есть", "футбол")

classmate = Classmate(
    "Alishka", "12.12.2006", "Frontend Developer", "есть", "Computer Science"
)

classmate2 = Classmate(
    "Meka", "01.10.2007", "Backend Developer", "нет", "Computer Science"
)

bestie = BestFriend(
    "Alinur", "14.01.2010", "---", "есть", "шахматы", "в детстве купались вместе"
)


people = [person, friend, friend1, classmate, classmate2, bestie]

for peop in people:
    
    peop.introduce()
