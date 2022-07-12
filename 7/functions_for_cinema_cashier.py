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

