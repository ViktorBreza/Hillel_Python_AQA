# Розробити функцію, котра приймає колекцію та обʼєкт функції, що приймає один аргумент. Певернути колекцію,
# кожен член якої є перетвореним членом вхідної колекції.
#
# # Нотатка. Обʼєкт функції, яку передаємо вказує на функцію, котра приймає один аргумент. Не користуватися функціями
# map чи filter!!!

def square_maker(sqr_atrib):
    """Takes in one attribute, returns the squared version of given attribute"""
    squared_data = [i ** 2 for i in sqr_atrib]
    return squared_data


def attribute_receiver(func, data_collection, *args, **kwargs):
    """Takes in function as attribute and some collection,
    returns call of the given function with given attributes"""
    print(f'Calling function with name {func.__name__}')
    return func(data_collection)


print(attribute_receiver(square_maker, [38, 2, 3, 4, 5]))
