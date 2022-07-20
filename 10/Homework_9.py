# Розробити клас Людина. Людина має:
#
# Ім'я
# Прізвище
# Вік (атрибут але ж змінний)
# Стать

# Люди можуть:
#
# Їсти Спати Говорити Ходити Стояти Лежати
# Також ми хочемо контролювати популяцію людства. Змінювати популяцію можемо в __init__.
# Треба сказати, що доступ до статичних полів класу з __init__ не можу іти через
# НазваКласу.статичий_атрибут, позаяк ми не може бачити імені класу. Але натомість ми можемо сказати
# self.__class__.static_attribute.
import datetime


class Human:
    population = 0

    def __init__(self, name, surname, sex, birth_date=datetime.date.today()):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.sex = sex
        self.__class__.increase_population()

    @classmethod
    def increase_population(cls):
        cls.population += 1
        print("Population has been increased by one human")

    @property
    def age(self):
        return(datetime.date.today() - self.birth_date).days // 365

    def eat(self, food):
        return f'{self.name} is eating {food}'

    def sleep(self):
        return f'{self.name} is sleeping'

    def talk(self):
        return f'{self.name} is speaking'

    def walk(self):
        return f'{self.name} is walking'

    def stand(self):
        return f'{self.name} is standing'

    def lay(self):
        return f'{self.name} is resting'


if __name__ == '__main__':

    anya = Human('Anna', 'Kravec', 'female', birth_date=datetime.date(1999, 2, 2))
    print(anya.age)
    print(anya.walk())
    print(anya.eat('meat'))
    print(anya.lay())

    nazar = Human('Nazarii', 'Kravec', 'male', birth_date=datetime.date(1992, 3, 8))
    print(nazar.stand())
    print(nazar.sleep())

    print(Human.population)