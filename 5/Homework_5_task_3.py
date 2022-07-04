# Напишіть функцію, що приймає два аргументи. Функція повинна
# якщо аргументи відносяться до числових типів - повернути різницю цих аргументів,
# якщо обидва аргументи це строки - обʼєднати в одну строку та повернути
# якщо перший строка, а другий ні - повернути dict де ключ це перший аргумент, а значення - другий
# у будь-якому іншому випадку повернути кортеж з цих аргументів


def arg_checker(arg1, arg2):
    """Takes in two arguments, returns the result according to the type of the arguments"""
    if isinstance(arg1, (int, float)) and isinstance(arg2, (int, float)):
        return arg1 - arg2
    elif isinstance(arg1, str) and isinstance(arg2, str):
        return arg1 + arg2
    elif isinstance(arg1, str) and not isinstance(arg2, str):
        arg_dict = {arg1: arg2}
        return arg_dict
    else:
        return arg1, arg2

