# Візьміть свою HW 6 ("Касир в кінотеатрі"), винесіть всі допоміжні функціі в окремий файл.
# В основному файлі виконайте імпорт цих функцій.

from functions_for_cinema_cashier import age_group_checking
from functions_for_cinema_cashier import customer_age
from functions_for_cinema_cashier import according_word


print(age_group_checking(customer_age))


#
if __name__ == '__main__':
    assert according_word in ("рік", "років", "роки"), "Wrong accompanying word"
    assert age_group_checking(123) == "Вам 123 роки? Покажіть пенсійне посвідчення!", "Wrong age group"  # Перед
    # запуском коду ввести в тест заплановане для вводу число та помістити відповідний шаблон f - строки
    # з функції age_group_checking, або закоментувати цей тест