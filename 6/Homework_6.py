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


def age_receiver():
    """Take in users input, check it for being integer and positive"""
    while True:
        try:
            received_age = int(input('Введіть, будь ласка, ваш вік у числовому форматі:\n'))
            if received_age > 0:
                break
            else:
                print('Число мусить бути більше нуля, спробуйте ще раз')
        except ValueError:
            print('Ваш вік мусить бути введений цілими числами за допомогою цифр!')
    return received_age


customer_age = age_receiver()

assert isinstance(customer_age, int), "Users input is not integer"


def correct_word_form(age):
    """Select the correct form of word "рік", according to inputted  number"""
    if 20 >= customer_age >= 10:
        return "років"
    elif str(customer_age).endswith(("2", "3")):
        return "роки"
    elif str(customer_age).endswith("1"):
        return "рік"
    else:
        return "років"


according_word = correct_word_form(customer_age)

assert according_word in ("рік", "років", "роки"), "Wrong accompanying word"


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
