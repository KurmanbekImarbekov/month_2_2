class Person:
    def __init__(self, name, birth_day, ocupation, higher_education):
        self.name = name
        self.birthday = birth_day
        self.ocupation = ocupation
        self.education = higher_education

    def introduce(self):
        print(
            f"Меня зовут {self.name} , я родился(лась) {self.birthday}, по професси {self.ocupation}, высшее оброзование {self.education}"
        )


class Classmate(Person):
    def __init__(self, name, birth_day, ocupation, higher_education, gropu_name):
        super().__init__(name, birth_day, ocupation, higher_education)
        self.gropu_name = gropu_name

    def introduce(self):
        print(
            f"Меня зовут {self.name}, и я являюсь одногруппником Байэля, я родился {self.birthday}, и работаю {self.ocupation},высшее оброзование {self.education},наша группа называется {self.gropu_name}"
        )


class Friend(Person):
    def __init__(self, name, birth_day, ocupation, higher_education, hobby):
        super().__init__(name, birth_day, ocupation, higher_education)
        self.hobby = hobby

    def introduce(self):
        print(
            f"Меня зовут {self.name}, и я являюсь другом Байэля, я родился {self.birthday},высшее оброзование {self.education} и работаю {self.ocupation}, мое хобби {self.hobby}"
        )


class BestFriend(Friend):
    def __init__(
        self, name, birth_day, ocupation, higher_education, hobby, shared_memory
    ):
        super().__init__(name, birth_day, ocupation, higher_education, hobby)
        self.shared_memory = shared_memory

    def introduce(self):
        parent_itro = super().introduce()
        return f"{parent_itro}, {self.shared_memory}"


person = Person("Kurmanbek", "17.10.2009", "ещё нет", "учусь")
friend = Friend("Dastan", "24.05.2010", "ещё нет", "есть", "рыбалка")
friend1 = Friend("Abadan", "17.06.2006", "Повар", "есть", "футбол")
classmate = Classmate(
    "Alishka", "12.12.06", "Frontend Developer", "есть", "Computer Since"
)
classmate2 = Classmate(
    "Meka", "01.10.2007", "Backend Developer", "нет", "Computer Since"
)
bestie = BestFriend(
    "Alinur", "14.01.2010", "---", "есть", "шахматы", "в детстве купались вместе"
)
friend.introduce()

classmate.introduce()

person.introduce()

bestie.introduce()

people = [person, friend, friend1, classmate, classmate2]
for peop in people:
    peop.introduce()
