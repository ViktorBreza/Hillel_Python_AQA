# Попросіть користувача ввести свсвій вік.
# # - якщо користувачу менше 7 - вивести "Тобі ж <>! Де твої батьки?"
# # - якщо користувачу менше 16 - вивести "Тобі лише <>, а це е фільм для дорослих!"
# # - якщо користувачу більше 65 - вивести "Вам <>? Покажіть пенсійне посвідчення!"
# # - якщо вік користувача складається з однакових цифр (11, 22, 44 і тд років, всі можливі варіанти!) - вивести "О,
# вам <>! Який цікавий вік!"
# # - у будь-якому іншому випадку - вивести "Незважаючи на те, що вам <>, білетів всеодно нема!"
#
# Замість <> в кожну відповідь підставте значення віку (цифру) та правильну форму слова рік
# # Для будь-якої відповіді форма слова "рік" має відповідати значенню віку користувача.
# # Наприклад :
# # "Тобі ж 5 років! Де твої батьки?"
# # "Вам 81 рік? Покажіть пенсійне посвідчення!"
# # "О, вам 33 роки! Який цікавий вік!"


class NotPositiveError(UserWarning):
    pass


def age_receiver():
    """Take in users input, check it for being positive integer"""
    while True:
        try:
            received_age = int(input('Введіть, будь ласка, ваш вік у числовому форматі:\n'))
            if received_age <= 0:
                raise NotPositiveError
            break
        except ValueError:
            print('Ваш вік мусить бути введений цілими числами за допомогою цифр!')
        except NotPositiveError:
            print('Число мусить бути більше нуля, спробуйте ще раз')
    return received_age


customer_age = age_receiver()


def correct_word_form(age):
    """Select the correct form of word "рік", according to inputted  number"""
    if customer_age % 10 == 1 and customer_age != 11 and customer_age % 100 != 11:
        return "рік"
    elif 1 < customer_age % 10 <= 4 and customer_age != 12 and customer_age != 13 and customer_age != 14:
        return "роки"
    else:
        return "років"


according_word = correct_word_form(customer_age)


def age_group_checking(age):
    """Choose the correct accompanying text according to inputted number"""
    if len(str(customer_age)) > 1:
        if str(customer_age) == len(str(customer_age)) * str(customer_age)[0]:
            return f'О, вам {customer_age} {according_word}! Який цікавий вік!!'
    if customer_age < 7:
        return f'Тобі ж {customer_age} {according_word}! Де твої батьки?'
    elif customer_age < 16:
        return f'Тобі лише {customer_age} {according_word}, а це фільм для дорослих!'
    elif customer_age > 65:
        return f'Вам {customer_age} {according_word}? Покажіть пенсійне посвідчення!'
    else:
        return f'Незважаючи на те, що вам {customer_age} {according_word}, білетів все одно нема!'


print(age_group_checking(customer_age))

if __name__ == '__main__':
    assert according_word in ("рік", "років", "роки"), "Wrong accompanying word"
    assert age_group_checking(123) == "Вам 123 роки? Покажіть пенсійне посвідчення!", "Wrong age group"  # Перед
    # запуском коду ввести в тест заплановане для вводу число та помістити відповідний шаблон f - строки
    # з функції age_group_checking, або закоментувати цей тест
