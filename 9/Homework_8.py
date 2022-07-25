# Створити клас Vehicle (транспортний засіб):
#
# ні від чого не наслідується
# в ініціалізатор класу (__init__ метод) передати
# producer: str
# model: str
# year: int
# tank_capacity: float # обєм паливного баку
# tank_level: float = 0 # початковий параметр рівня паливного баку дорівнює 0, параметр в аргументах не передавати
# maxspeed: int
# fuel_consumption: float # litres/100km споживання пального
# odometer_value: int = 0 # при сході з конвеєра пробіг нульовий, параметр в аргументах не передавати
#
# # визначити метод __repr__, яким повертати інформаційну стрічку (наповнення на ваш вибір, проте параметри model and
# year and odometer_value мають бути передані
# #
# написати метод refueling, який не приймає жодного аргумента, заправляє автомобіль на уявній автозаправці до
# максимума (tank_level = tank_capacity), після чого виводить на екран повідомлення, скільки літрів було заправлено (
# перша заправка буде повного баку, а в інших випадках величина буде залежати від залишку пального в баку)
#
# # написати метод race, який приймає один аргумент (не враховуючи self) - відстань, яку потрібно проїхати, а повертає
# словник, в якому вказано, скільки авто проїхало, з огляду на заповнення паливного баку перед поїздкою,
# залишок пального (при малому кілометражі все пальне не використається), та час, за який відбулася дана поїздка,
# з урахування, що середня швидкість складає 80% від максимальної (витрата пального рівномірна незалежно від швидкості)
#
# за результатами роботи метода в атрибуті tank_level екземпляра класа має зберігатися залишок пального після поїздки
# (зрозуміло, що не менше 0)
#
# збільшити на величину поїздки показники odometer_value
#
# # написати метод lend_fuel, який приймає окрім self ще й other обєкт, в результаті роботи якого паливний бак обєкта,
# на якому було викликано відповідний метод, наповнюється до максимального рівня за рахунок відповідного зменшення
# рівня пального у баку дружнього транспортного засобу
#
# вивести на екран повідомлення з текстом типу "Дякую, бро, виручив. Ти залив мені *** літрів пального"
#
# у випадку, якщо бак першого обєкта повний або у другого обєкта немає пального, вивести повідомлення "Нічого
# страшного, якось розберуся"
# #
# написати метод get_tank_level, для отримання інформації про залишок пального конкретного інсттанса
#
# # # написати метод get_mileage, який поверне значення пробігу odometer_value
# #
# написати метод __eq__, який приймає окрім self ще й other обєкт (реалізація магічного методу для оператора
# порівняння == )
#
# даний метод має повернути True у випадку, якщо 2 обєкта, які порівнюються, однакові за показниками року випуску та
# пробігу (значення відповідних атрибутів однакові, моделі можуть бути різними)
#
# # створіть не менше 2-х обєктів класу, порівняйте їх до інших операцій, заправте їх, покатайтесь на них на різну
# відстань, перевірте пробіг, позичте один в одного пальне, знову порівняйте


class Vehicle:
    def __init__(self, producer, model, year, tank_capacity, maxspeed, fuel_consumption, *args, **kwargs):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.maxspeed = maxspeed
        self.fuel_consumption = fuel_consumption
        self.__tank_level = 0
        self.__odometer_value = 0

    def get_tank_level(self):
        """показує інформацію про залишок пального"""
        return self.__tank_level

    def get_mileage(self):
        """повертає значення пробігу odometer_value """
        return self.__odometer_value

    def set_tank_level(self, level):
        self.__tank_level = level

    def set_mileage(self, mileage):
        self.__odometer_value = mileage

    def __repr__(self):
        """повертає інформаційну стрічку про даний об'єкт класу"""
        return (
            f"This car {self.producer} {self.model} was produced in {self.year}. "
            f"Now its odometer value is {self.__odometer_value} km. "
            f" Other properties are: tank capacity - {self.tank_capacity} litres, max speed - {self.maxspeed}, "
            f"fuel consumption - {self.fuel_consumption} litres/100 km")

    def refueling(self):
        """заправляє автомобіль на уявній автозаправці до максимума, після чого виводить на екран повідомлення,
        скільки літрів було заправлено (перша заправка буде повного баку, а в інших випадках величина буде залежати
        від залишку пального в баку) """
        fuel_volume = self.tank_capacity - self.get_tank_level()
        self.set_tank_level(self.tank_capacity)
        return f"Refueled with {fuel_volume} litres of fuel"

    def race(self, distance):
        """приймає один аргумент - відстань, яку потрібно проїхати, а повертає
    словник, в якому вказано, скільки авто проїхало, з огляду на заповнення паливного баку перед поїздкою,
    залишок пального, та час, за який відбулася дана поїздка,
    з урахування, що середня швидкість складає 80% від максимальної """
        result = {}
        fuel_consumption_per_km = (self.fuel_consumption * 0.8) / 100

        total_fuel_consumption = distance * fuel_consumption_per_km

        if total_fuel_consumption > self.get_tank_level():
            passed_distance = self.__tank_level * fuel_consumption_per_km
            self.set_tank_level(0)
        else:
            passed_distance = distance
            self.set_tank_level(self.get_tank_level() - total_fuel_consumption)

        result["Passed distance"] = passed_distance
        result["Fuel rest"] = self.get_tank_level()
        result["Time"] = passed_distance / (self.maxspeed * 0.8)
        self.__odometer_value = self.__odometer_value + passed_distance

        return result

    # написати метод lend_fuel, який приймає окрім self ще й other обєкт, в результаті роботи якого паливний бак обєкта,
    # на якому було викликано відповідний метод, наповнюється до максимального рівня за рахунок відповідного
    # зменшення рівня пального у баку дружнього транспортного засобу вивести на екран повідомлення з текстом типу
    # "Дякую, бро, виручив. Ти залив мені *** літрів пального" у випадку, якщо бак першого обєкта повний або у
    # другого обєкта немає пального, вивести повідомлення "Нічого страшного, якось розберуся"
    def lend_fuel(self, other):
        """паливний бак об'єкта наповнюється до максимального рівня за рахунок відповідного
    зменшення рівня пального у баку дружнього транспортного засобу , якщо бак першого об'єкта повний або у
    другого обєкта немає пального, виводить повідомлення "Нічого страшного, якось розберуся"""
        fuel_volume = self.tank_capacity - self.get_tank_level()

        if other.get_tank_level() > fuel_volume:
            lended_fuel = fuel_volume
            self.set_tank_level(self.tank_capacity)
            other.set_tank_level(other.get_tank_level() - lended_fuel)
        else:
            lended_fuel = other.get_tank_level()
            other.set_tank_level(0)

        print(f"Дякую, бро, виручив. Ти залив мені {int(lended_fuel)} літрів пального")

        if self.get_tank_level() == self.tank_capacity and other.get_tank_level() == 0:
            print("Нічого страшного, якось розберуся")

    # написати метод eq, який приймає окрім self ще й other обєкт (реалізація магічного методу для оператора
    # порівняння == ) даний метод має повернути True у випадку, якщо 2 обєкта, які порівнюються, однакові за
    # показниками року випуску та пробігу (значення відповідних атрибутів однакові, моделі можуть бути різними)
    def eq(self, other):
        """повертає True у випадку, якщо 2 обєкта, які порівнюються, однакові за
           показниками року випуску та пробігу"""
        return self.year == other.year and self.get_mileage() == other.get_mileage()


if __name__ == '__main__':
    first_car = Vehicle("Skoda", "Octavia", 2015, 50, 220, 6.5)
    print(first_car.refueling())
    print(first_car.race(150))
    print(first_car.get_tank_level())
    print(repr(first_car))

    second_car = Vehicle("Audi", "A6", 2019, 75, 280, 8)
    print(second_car.refueling())
    print(second_car.race(300))
    second_car.lend_fuel(first_car)
    print(second_car.eq(first_car))

    third_car = Vehicle("Volkswagen ", "Touareg", 2015, 90, 250, 9)
    print(third_car.refueling())
    print(third_car.race(150))
    print(third_car.get_tank_level())
    print(third_car.eq(first_car))
